from __future__ import annotations

import copy
import json
import re
from typing import Dict, Iterable, List, Optional, Tuple, Type, TypeVar, Union

from ..model import AriadneBaseModel
from ..util import deprecated, gen_subclass
from .element import (
    At,
    AtAll,
    Element,
    File,
    MultimediaElement,
    NotSendableElement,
    Plain,
    Quote,
    Source,
    _update_forward_refs,
)

MessageIndex = Tuple[int, Optional[int]]

Element_T = TypeVar("Element_T", bound=Element)

ELEMENT_MAPPING = {
    i.__fields__["type"].default: i
    for i in gen_subclass(Element)
    if hasattr(i.__fields__["type"], "default")
}


class MessageChain(AriadneBaseModel):
    """
    即 "消息链", 被用于承载整个消息内容的数据结构, 包含有一有序列表, 包含有继承了 Element 的各式类实例.
    """

    __root__: List[Element]

    @staticmethod
    def build_chain(obj: List[Union[dict, Element, str]]) -> List[Element]:
        """内部接口, 会自动反序列化对象并生成.

        Args:
            obj (List[T]): 需要反序列化的对象

        Returns:
            List[Element]: 内部承载有尽量有效的消息元素的列表
        """
        element_list: List[Element] = []
        for i in obj:
            if isinstance(i, Element):
                element_list.append(i)
            elif isinstance(i, dict) and "type" in i:
                for element_cls in gen_subclass(Element):
                    if element_cls.__name__ == i["type"]:
                        element_list.append(element_cls.parse_obj(i))
                        break
            elif isinstance(i, str):
                element_list.append(Plain(i))
        return element_list

    @classmethod
    def parse_obj(
        cls: Type["MessageChain"], obj: List[Union[dict, Element]]
    ) -> "MessageChain":
        """内部接口, 会自动将作为外部态的消息元素转为内部态.

        Args:
            obj (List[T]): 需要反序列化的对象

        Returns:
            MessageChain: 内部承载有尽量有效的消息元素的消息链
        """
        return cls(__root__=cls.build_chain(obj))

    def __init__(self, __root__: Iterable[Union[Element, str]]) -> None:
        super().__init__(__root__=self.build_chain(__root__))

    @classmethod
    def create(
        cls, *elements: Union[Iterable[Element], Element, str]
    ) -> "MessageChain":
        """
        创建消息链.
        比起直接实例化, 本方法拥有更丰富的输入实例类型支持.

        Args:
            *elements(Union[Iterable[Element], Element, str]): 元素的容器, 为承载元素的可迭代对象/单元素实例,
            字符串会被自动不可逆的转换为 `Plain`
        """

        element_list = []
        for i in elements:
            if isinstance(i, Element):
                element_list.append(i)
            elif isinstance(i, str):
                element_list.append(Plain(i))
            else:
                element_list.extend(list(i))
        return cls(__root__=element_list)

    def prepare(self, copy: bool = False) -> "MessageChain":
        """
        对消息链中所有元素进行处理.

        Returns:
            MessageChain: copy = True 时返回副本, 否则返回自己的引用.
        """
        chain_ref = self.copy() if copy else self
        chain_ref.merge()
        for i in chain_ref.__root__[:]:
            try:
                i.prepare()
            except NotSendableElement:
                chain_ref.__root__.remove(i)
        if copy:
            return chain_ref
        else:
            return self

    def has(self, element_class: Type[Element_T]) -> bool:
        """
        判断消息链中是否含有特定类型的消息元素

        Args:
            element_class (T): 需要判断的消息元素的类型, 例如 "Plain", "At", "Image" 等.

        Returns:
            bool: 判断结果
        """
        return element_class in [type(i) for i in self.__root__]

    def get(self, element_class: Type[Element_T]) -> List[Element_T]:
        """
        获取消息链中所有特定类型的消息元素

        Args:
            element_class (T): 指定的消息元素的类型, 例如 "Plain", "At", "Image" 等.

        Returns:
            List[T]: 获取到的符合要求的所有消息元素; 另: 可能是空列表([]).
        """
        return [i for i in self.__root__ if isinstance(i, element_class)]

    def getOne(self, element_class: Type[Element_T], index: int) -> Element_T:
        """
        获取消息链中第 index + 1 个特定类型的消息元素

        Args:
            element_class (Type[Element_T]): 指定的消息元素的类型, 例如 "Plain", "At", "Image" 等.
            index (int): 索引, 从 0 开始数

        Returns:
            Element_T: 消息链第 index + 1 个特定类型的消息元素
        """
        return self.get(element_class)[index]

    def getFirst(self, element_class: Type[Element_T]) -> Element_T:
        """
        获取消息链中第 1 个特定类型的消息元素

        Args:
            element_class (Type[Element_T]): 指定的消息元素的类型, 例如 "Plain", "At", "Image" 等.

        Returns:
            Element_T: 消息链第 1 个特定类型的消息元素
        """
        return self.getOne(element_class, 0)

    def asDisplay(self) -> str:
        """
        获取以字符串形式表示的消息链, 且趋于通常你见到的样子.

        Returns:
            str: 以字符串形式表示的消息链
        """
        return "".join(i.asDisplay() for i in self.__root__)

    def __contains__(self, item: Union[Type[Element_T], str]) -> bool:
        """
        是否包含特定元素类型/字符串
        """
        if isinstance(item, str):
            return self.hasText(item)
        else:
            return self.has(item)

    def __getitem__(
        self, item: Union[Type[Element_T], slice, Tuple[Type[Element_T], int]]
    ) -> Union[List[Element_T], "MessageChain", Element]:
        """
        可通过切片取出子消息链, 或元素.

        通过 `type, count` 型元组取出前 `count` 个 `type` 元素组成的列表

        通过 `type` 取出属于 `type` 的元素列表

        通过 `int` 取出对应位置元素.

        Args:
            item (Union[Type[Element_T], slice, Tuple[Type[Element_T], int]]): 索引项
        Returns:
            Union[List[Element_T], "MessageChain", Element]: 索引结果.
        """
        if isinstance(item, slice):
            return self.subchain(item)
        elif isinstance(item, type) and issubclass(item, Element):
            return self.get(item)
        elif isinstance(item, tuple):
            return self.get(item[0])[: item[1]]
        elif isinstance(item, int):
            return self.__root__[item]
        else:
            raise NotImplementedError(
                "{0} is not allowed for item getting".format(type(item))
            )

    def subchain(self, item: slice, ignore_text_index: bool = False) -> "MessageChain":
        """对消息链执行分片操作

        Args:
            item (slice): 这个分片的 `start` 和 `end` 的 Type Annotation 都是 `Optional[MessageIndex]`

        Raises:
            TypeError: TextIndex 取到了错误的位置

        Returns:
            MessageChain: 分片后得到的新消息链, 绝对是原消息链的子集.
        """

        result = copy.copy(self.__root__)
        if item.start:
            first_slice = result[item.start[0] :]
            if item.start[1] is not None and first_slice:  # text slice
                if not isinstance(first_slice[0], Plain):
                    if not ignore_text_index:
                        raise TypeError(
                            "the sliced chain does not starts with a Plain: {}".format(
                                first_slice[0]
                            )
                        )
                    else:
                        result = first_slice
                else:
                    final_text = first_slice[0].text[item.start[1] :]
                    result = [
                        *([Plain(final_text)] if final_text else []),
                        *first_slice[1:],
                    ]
            else:
                result = first_slice
        if item.stop:
            first_slice = result[: item.stop[0]]
            if item.stop[1] is not None and first_slice:  # text slice
                if not isinstance(first_slice[-1], Plain):
                    raise TypeError(
                        "the sliced chain does not ends with a Plain: {}".format(
                            first_slice[-1]
                        )
                    )
                final_text = first_slice[-1].text[: item.stop[1]]
                result = [
                    *first_slice[:-1],
                    *([Plain(final_text)] if final_text else []),
                ]
            else:
                result = first_slice
        return MessageChain(result)

    def exclude(self, *types: Type[Element]) -> MessageChain:
        """将除了在给出的消息元素类型中符合的消息元素重新包装为一个新的消息链

        Args:
            *types (Type[Element]): 将排除在外的消息元素类型

        Returns:
            MessageChain: 返回的消息链中不包含参数中给出的消息元素类型
        """
        return MessageChain([i for i in self.__root__ if type(i) not in types])

    def include(self, *types: Type[Element]) -> MessageChain:
        """将只在给出的消息元素类型中符合的消息元素重新包装为一个新的消息链

        Args:
            *types (Type[Un]): 将只包含在内的消息元素类型

        Returns:
            MessageChain: 返回的消息链中只包含参数中给出的消息元素类型
        """
        return MessageChain([i for i in self.__root__ if type(i) in types])

    def split(self, pattern: str, raw_string: bool = False) -> List["MessageChain"]:
        """和 `str.split` 差不多, 提供一个字符串, 然后返回分割结果.

        Returns:
            List["MessageChain"]: 分割结果, 行为和 `str.split` 差不多.
        """

        result: List["MessageChain"] = []
        tmp = []
        for element in self.__root__:
            if isinstance(element, Plain):
                split_result = element.text.split(pattern)
                for index, split_str in enumerate(split_result):
                    if tmp and index > 0:
                        result.append(MessageChain(tmp))
                        tmp = []
                    if split_str or raw_string:
                        tmp.append(Plain(split_str))
            else:
                tmp.append(element)
        else:
            if tmp:
                result.append(MessageChain(tmp))
                tmp = []
        return result

    def __repr__(self) -> str:
        return f"MessageChain({repr(self.__root__)})"

    def __iter__(self) -> Iterable[Element]:
        return iter(self.__root__)

    def startswith(self, string: str) -> bool:
        """
        判定消息链是否以相应字符串开头

        Args:
            string (str): 需要判断的字符串

        Returns:
            bool: 是否以此字符串开头
        """

        if not self.__root__ or type(self.__root__[0]) is not Plain:
            return False
        return self.__root__[0].text.startswith(string)

    def endswith(self, string: str) -> bool:
        """
        判定消息链是否以相应字符串结尾

        Args:
            string (str): 需要判断的字符串

        Returns:
            bool: 是否以此字符串结尾
        """

        if not self.__root__ or type(self.__root__[-1]) is not Plain:
            return False
        last_element: Plain = self.__root__[-1]
        return last_element.text.endswith(string)

    def hasText(self, string: str) -> bool:
        """
        判定消息链内是否包括相应字符串

        Args:
            string (str): 需要判断的字符串

        Returns:
            bool: 是否包括
        """

        for i in self.merge(copy=True).get(Plain):
            if string in i.text:
                return True
        return False

    @deprecated("0.4.0")
    def onlyHas(self, *types: Type[Element]) -> bool:
        return all(isinstance(i, types) for i in self.__root__)

    def onlyContains(self, *types: Type[Element]) -> bool:
        return all(isinstance(i, types) for i in self.__root__)

    def merge(self, copy: bool = False) -> "MessageChain":
        """
        在实例内合并相邻的 Plain 项

        copy (bool): 是否要在副本上修改.
        Returns:
            MessageChain: copy = True 时返回副本, 否则返回自己的引用.
        """

        result = []

        plain = []
        for i in self.__root__:
            if not isinstance(i, Plain):
                if plain:
                    result.append(Plain("".join(plain)))
                    plain.clear()  # 清空缓存
                result.append(i)
            else:
                plain.append(i.text)
        else:
            if plain:
                result.append(Plain("".join(plain)))
                plain.clear()
        if copy:
            return MessageChain(result)
        else:
            self.__root__ = result
            return self

    def append(self, element: Element) -> None:
        """
        向消息链最后追加单个元素
        """
        self.__root__.append(element)

    def extend(
        self, *content: Union[MessageChain, Element, List[Element]], copy: bool = False
    ) -> "MessageChain":
        """
        向消息链最后添加元素/元素列表/消息链
        Args:
            *content (Union[MessageChain, Element, List[Element]])：要添加的元素/元素容器.
            copy (bool): 是否要在副本上修改.

        Returns:
            MessageChain: copy = True 时返回副本, 否则返回自己的引用.
        """
        result = []
        for i in content:
            if isinstance(i, Element):
                result.append(i)
            if isinstance(i, MessageChain):
                result.extend(i.__root__)
            else:
                result.extend(i)
        if copy:
            return MessageChain(result)
        else:
            self.__root__ = result
            return self

    def copy(self) -> "MessageChain":
        """
        拷贝本消息链.
        Returns:
            MessageChain: 拷贝的副本.
        """
        return MessageChain(self.__root__)

    def index(self, element_type: Type[Element_T]) -> Union[int, None]:
        """
        寻找第一个特定类型的元素, 并返回其下标.
        """
        for i, e in enumerate(self.__root__):
            if isinstance(e, element_type):
                return i

    def count(self, element_type: Type[Element_T]) -> int:
        """
        统计共有多少个指定类型的元素.
        """
        cnt = 0
        for e in self.__root__:
            if isinstance(e, element_type):
                cnt += 1
        return cnt

    def asSendable(self):
        return self.exclude(Source, Quote, File)

    def __add__(self, content: Union[MessageChain, List[Element]]) -> "MessageChain":
        if isinstance(content, MessageChain):
            content: List[Element] = content.__root__
        return MessageChain(self.__root__ + content)

    def __iadd__(self, content: Union[MessageChain, List[Element]]) -> "MessageChain":
        if isinstance(content, MessageChain):
            content: List[Element] = content.__root__
        self.__root__.extend(content)
        return self

    def __mul__(self, time: int) -> "MessageChain":
        return MessageChain(self.__root__ * time)

    def __imul__(self, time: int) -> "MessageChain":
        self.__root__ *= time
        return self

    def __len__(self) -> int:
        return len(self.__root__)

    def asPersistentString(
        self,
        *,
        binary: bool = True,
        include: Optional[Iterable[Type[Element]]] = (),
        exclude: Optional[Iterable[Type[Element]]] = (),
    ) -> str:
        """转换为持久化字符串.

        Args:
            binary (bool, optional): 是否附带图片或声音的二进制. 默认为 True.
            include (Optional[Iterable[Type[Element]]], optional): 筛选, 只包含本参数提供的元素类型.
            exclude (Optional[Iterable[Type[Element]]], optional): 筛选, 排除本参数提供的元素类型.

        Raises:
            ValueError: 同时提供 include 与 exclude

        Returns:
            str: 持久化字符串. 不是 Mirai Code.
        """
        string_list = []
        include = tuple(include)
        exclude = tuple(exclude)
        if include and exclude:
            raise ValueError("Can not present include and exclude at same time!")
        for i in self.__root__:
            if (
                (include and isinstance(i, include))
                or (exclude and isinstance(i, exclude))
                or not (include or exclude)
            ):
                if isinstance(i, Plain):
                    string_list.append(i.asPersistentString().replace("[", "[_"))
                elif not isinstance(i, MultimediaElement) or binary:
                    string_list.append(i.asPersistentString())
                else:
                    string_list.append(i.asPersistentString(binary=False))
        return "".join(string_list)

    async def download_binary(self) -> None:
        """下载消息中所有的二进制数据并保存在元素实例内"""
        for elem in self.__root__:
            if isinstance(elem, MultimediaElement):
                await elem.get_bytes()

    @classmethod
    def fromPersistentString(cls, string: str) -> "MessageChain":
        """从持久化字符串生成消息链.

        Returns:
            MessageChain: 还原的消息链.
        """
        result = []
        for match in re.split(r"(\[mirai:.+?\])", string):
            mirai = re.fullmatch(r"\[mirai:(.+?)(:(.+?))\]", match)
            if mirai:
                j_string = mirai.group(3)
                element_cls = ELEMENT_MAPPING[mirai.group(1)]
                result.append(element_cls.parse_obj(json.loads(j_string)))
            elif match:
                result.append(Plain(match.replace("[_", "[")))
        return MessageChain.create(result)

    def asMappingString(
        self,
        *,
        remove_source: bool = True,
        remove_quote: bool = True,
        remove_extra_space: bool = False,
    ) -> Tuple[str, Dict[int, Element]]:
        """转换消息链为映射字符串与映射字典的元组.

        Args:
            remove_source (bool, optional): 是否移除消息链中的 Source 元素. 默认为 True.
            remove_quote (bool, optional): 是否移除消息链中的 Quote 元素. 默认为 True.
            remove_extra_space (bool, optional): 是否移除 Quote At AtAll 的多余空格. 默认为 False.

        Returns:
            Tuple[str, Dict[int, Element]]: 生成的映射字符串与映射字典的元组
        """
        elem_mapping: Dict[int, Element] = {}
        elem_str_list: List[str] = []
        for i, elem in enumerate(self.__root__):
            if not isinstance(elem, Plain):
                if remove_quote and isinstance(elem, Quote):
                    continue
                elif remove_source and isinstance(elem, Source):
                    continue
                elem_mapping[i] = elem
                elem_str_list.append(f"\b{i}_{elem.type}\b")
            else:
                if (
                    remove_extra_space
                    and i  # not first element
                    and isinstance(
                        self.__root__[i - 1], (Quote, At, AtAll)
                    )  # following elements which have an dumb trailing space
                    and elem.text.startswith("  ")  # extra space (count >= 2)
                ):
                    elem_str_list.append(elem.text[1:])
                else:
                    elem_str_list.append(elem.text)
        return "".join(elem_str_list), elem_mapping

    @classmethod
    def fromMappingString(
        cls, string: str, mapping: Dict[int, Element]
    ) -> "MessageChain":
        """从映射字符串与映射字典的元组还原消息链.

        Args:
            string (str): 映射字符串
            mapping (Dict[int, Element]): 映射字典.

        Returns:
            MessageChain: 构建的消息链
        """
        elements: List[Element] = []
        for x in re.split("(\b\\d+_\\w+\b)", string):
            if match := re.match("\b(\\d+)_\\w+\b", x):
                index = int(match.group(1))
                elements.append(mapping[index])
            else:
                if x:
                    elements.append(Plain(x))
        return cls.create(elements)

    def removeprefix(self, prefix: str, *, copy: bool = True) -> "MessageChain":
        """移除消息链前缀.

        Args:
            prefix (str): 要移除的前缀.
            copy (bool, optional): 是否在副本上修改, 默认为 True.

        Returns:
            MessageChain: 修改后的消息链, 若未移除则原样返回.
        """
        elements = self.__root__[:]
        if not elements or not isinstance(elements[0], Plain):
            return self if not copy else self.copy()
        if elements[0].text.startswith(prefix):
            elements[0].text = elements[0].text[len(prefix) :]
            if copy:
                return MessageChain.create(elements)
            else:
                self.__root__ = elements

    def removesuffix(self, suffix: str, *, copy: bool = True) -> "MessageChain":
        """移除消息链后缀.

        Args:
            prefix (str): 要移除的后缀.
            copy (bool, optional): 是否在副本上修改, 默认为 True.

        Returns:
            MessageChain: 修改后的消息链, 若未移除则原样返回.
        """
        elements = self.__root__[:]
        if not elements or not isinstance(elements[-1], Plain):
            return self if not copy else self.copy()
        last_elem: Plain = elements[-1]
        if last_elem.text.endswith(suffix):
            last_elem.text = last_elem.text[: -len(suffix)]
            if copy:
                return MessageChain.create(elements)
            else:
                self.__root__ = elements


_update_forward_refs()
