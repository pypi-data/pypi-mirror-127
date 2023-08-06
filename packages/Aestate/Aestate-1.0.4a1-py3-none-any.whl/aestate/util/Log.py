import datetime
import os
import sys
import threading
from aestate.work.Modes import Singleton
from aestate.exception import e_fields
from aestate.util import others
from aestate.work.commad import __logo__


class FieldsLength:
    DATETIME_FORMAT = 24
    INFO_FORMAT = 5
    LINE_FORMAT = 5
    OPERATION_FORMAT = 14
    # HEX_FORMAT = 17
    TASK_FORMAT = 10
    # CLASS_FORMAT = 70
    MSG_FORMAT = 0


class ConsoleColor:
    """
    控制台类型
    """

    class FontColor:
        # 黑色
        BLACK = 30
        # 灰色
        GRAY = 90
        # 粉色
        PINK = 31
        # 红色
        RED = 35
        # 绿色
        GREEN = 32
        # 浅绿色
        LIGHT_GREEN = 91
        # 黄色
        YELLOW = 33
        # 浅黄色
        LIGHT_YELLOW = 92
        # 深黄色
        DARK_YELLOW = 93
        # 紫色
        PURPLE = 34
        # 浅紫色
        LIGHT_PURPLE = 96
        # 青蓝色
        CYAN = 36
        # 白色
        WHITE = 37
        # 成功的颜色 和 info的颜色
        SUCCESS_COLOR = GREEN
        # 失败的颜色 和 错误的颜色
        ERROR_COLOR = RED
        # 警告的颜色
        WARNING_COLOR = YELLOW

    class BackgroundColor:
        # 黑色
        BLACK = 40
        # 红色
        RED = 41
        # 绿色
        GREEN = 42
        # 黄色
        YELLOW = 43
        # 蓝色
        BLUE = 44
        # 紫红色
        FUCHSIA = 45
        # 青蓝色
        CYAN = 46
        # 白色
        WHITE = 47

    class ShowType:
        # 默认
        DEFAULT = 0
        # 高亮
        HIGHLIGHT = 1
        # 下划线
        UNDERSCORE = 4
        # 闪烁
        FLASHING = 5
        # 反显
        REVERSE = 7
        # 不可见
        INVISIBLE = 8


class ConsoleWrite:
    def __init__(self):
        self.fontColor = ConsoleColor.FontColor.GREEN
        self.showType = ConsoleColor.ShowType.DEFAULT
        self.backColor = None

    # @staticmethod
    # def write(messages, consoleWriteObj=None):
    #     prefix = "{};".format(consoleWriteObj.showType) if consoleWriteObj.showType is not None else ""
    #     center = ";".format(consoleWriteObj.backColor) if consoleWriteObj.backColor is not None else ""
    #     suffix = "{}m{}".format(consoleWriteObj.fontColor, messages)
    #     out = "\033[{}{}{}\033[0m".format(prefix, center, suffix)
    #     print(out)

    @staticmethod
    def format_color(text, color):
        prefix = "{};".format(ConsoleColor.ShowType.DEFAULT)
        suffix = "{}m{}".format(color, text)
        out = "\033[{};{}\033[0m".format(prefix, suffix)
        return out


def write(path, content, max_size):
    """
    写出文件
    :param path:位置
    :param content:内容
    :param max_size:文件保存的最大限制
    :return:
    """
    _sep_path = path.split(os.sep)
    _path = ''
    for i in _sep_path:
        _end = _sep_path[len(_sep_path) - 1]
        if i != _end:
            _path += str(i) + os.sep
        else:
            _path += str(i)
        if not os.path.exists(_path):
            if '.' not in i:
                os.makedirs(_path)

    content += '\n'
    with open(os.path.join(_path), mode="a", encoding="UTF-8") as f:
        f.write(content)
        f.close()
    _size = os.path.getsize(_path)
    if _size >= max_size:
        os.remove(_path)
        # 递归
        write(path, content, max_size)


class ALog(object):
    _instance_lock = threading.RLock()

    def __init__(self, path, print_flag=False, save_flag=False, max_clear=10):
        """

        初始化配置

        :param path:保存的路径

        :param print_flag:是否打印日志 默认False

        :param save_flag:是否保存日志 默认False

        :param max_clear:日志储存最大限制,默认10MB 单位:MB

        """
        # bug
        self.max_clear = max_clear * 1024 * 1000
        self.path = path
        self.print_flag = print_flag
        self.save_flag = save_flag
        self.__info_logo_show__ = False
        self.__warn_logo_show__ = False
        self.__error_logo_show__ = False

    @staticmethod
    def pure_log(msg, **kwargs):
        """
        输出任务执行日志

        :param msg:消息

        """
        ALog.log(msg=msg, **kwargs)

    @staticmethod
    def log(msg, obj=None, line=sys._getframe().f_back.f_lineno,
            task_name='Task', LogObject=None, field: e_fields.LogStatus = e_fields.LogStatus.Info, func=None, **kwargs):
        """
        输出任务执行日志

        :param obj:执行日志的对象地址
        :param msg:消息
        :param line:被调用前的行数
        :param task_name:任务对象的值
        :param LogObject:写出文件的对象
        :param field:日志模式
        :param func:日志执行后的自定义操作
        """

        t = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        try:
            if obj is not None:
                write_repr = others.fullname(obj)
                # if write_repr == 'type':
                #     write_repr = obj.__base__.__module__ + '.' + obj.__base__.__name__
            else:
                write_repr = 'OBJECT IS NULL'
        except TypeError as err:
            write_repr = 'OBJECT CAN`T NOT PARSE'

        # write_repr = repr if repr and not repr_c else repr_c[0] if repr_c else type(obj)
        # 格式：时间 类型 日志名称 对象地址 被调用行号 执行类型 信息

        con_text = ' '.join([str(t), str(field), str(line), str(hex(id(obj))),
                             '[{}]'.format(task_name), str(write_repr), f" : {msg}"])

        t = ConsoleWrite.format_color(f"{t}".ljust(FieldsLength.DATETIME_FORMAT), ConsoleColor.FontColor.CYAN)
        _field = ConsoleWrite.format_color(f"{field.value}".rjust(FieldsLength.INFO_FORMAT),
                                           ConsoleColor.FontColor.GREEN
                                           if field == e_fields.LogStatus.Info
                                           else ConsoleColor.FontColor.RED
                                           if field == e_fields.LogStatus.Error
                                           else ConsoleColor.FontColor.YELLOW
                                           if field == e_fields.LogStatus.Warn
                                           else ConsoleColor.FontColor.YELLOW)
        line = f"{line}".rjust(FieldsLength.LINE_FORMAT)
        hex_id = ConsoleWrite.format_color(f" {str(hex(id(obj)))}", ConsoleColor.FontColor.PINK)
        task_name = f"{task_name}".rjust(FieldsLength.TASK_FORMAT)
        write_repr = ConsoleWrite.format_color(write_repr, ConsoleColor.FontColor.LIGHT_GREEN)
        msg = f" : {msg}"

        info = "{}{}{}{}{}{}{}".format(t, field, line, hex_id, ' [{}] '.format(task_name), write_repr, msg)
        print(info)
        if LogObject is not None:
            _path = "%s%s%s%s" % (os.sep, str(field.value).lower(), os.sep, 'log.log')
            logo_show = False
            if field == e_fields.LogStatus.Info:
                logo_show = LogObject.__info_logo_show__
            elif field == e_fields.LogStatus.Error:
                logo_show = LogObject.__error_logo_show__
            elif field == e_fields.LogStatus.Warn:
                logo_show = LogObject.__warn_logo_show__
            if not logo_show:
                if field == e_fields.LogStatus.Info:
                    LogObject.__info_logo_show__ = True
                elif field == e_fields.LogStatus.Error:
                    LogObject.__error_logo_show__ = True
                elif field == e_fields.LogStatus.Warn:
                    LogObject.__warn_logo_show__ = True
                else:
                    LogObject.__info_logo_show__ = True
                LogObject.log_util(_path, __logo__)
            LogObject.log_util(_path, con_text)

        if func is not None:
            func(con_text)

        return info

    @staticmethod
    def warning(msg, obj=None, line=sys._getframe().f_back.f_lineno, task_name='WARNING', LogObject=None):

        consoleWrite = ConsoleWrite()
        consoleWrite.fontColor = ConsoleColor.FontColor.WARNING_COLOR

        ALog.log(msg=msg, obj=obj, line=line, task_name=task_name, LogObject=LogObject, field=e_fields.LogStatus.Warn,
                 func=LogObject)

    @staticmethod
    def log_error(msg, obj=None, line=sys._getframe().f_back.f_lineno, task_name='ERROR', LogObject=None,
                  raise_exception=False):
        """
        :param msg:描述
        :param line:行
        :param obj:执行的对象，当允许抛出异常时，则指明该对象为一个Exception或他的子类
        :param task_name:线程唯一名称
        :param LogObject:日志对象
        :param raise_exception:是否抛出异常
        """
        ALog.log(msg=msg, obj=obj, line=line, task_name=task_name, LogObject=LogObject, field=e_fields.LogStatus.Error,
                 func=LogObject.warn if LogObject is not None else None)

        if raise_exception:
            raise obj(msg)

    @staticmethod
    def err(cls, msg, LogObject=None):
        if LogObject is not None:
            LogObject.error(msg)
        raise cls(msg)

    def success(self, content):
        """
        成功日志
        :param content:内容
        :return:
        """
        _path = "%s%s%s%s" % (os.sep, 'success', os.sep, 'log.log')
        if not self.__info_logo_show__:
            self.__info_logo_show__ = True
            self.log_util(_path, __logo__)
        self.log_util(_path, content)

    def error(self, content):
        """
        错误日志
        :param content:内容
        :return:
        """
        _path = "%s%s%s%s" % (os.sep, 'error', os.sep, 'log.log')
        self.log_util(_path, content)

    def warn(self, content):
        """
        警告日志
        :param content:内容
        :return:
        """
        _path = "%s%s%s%s" % (os.sep, 'warn', os.sep, 'log.log')
        self.log_util(_path, content)

    def log_util(self, path_str, content):
        """
        日志工具,勿用
        :param path_str:
        :param content:
        :return:
        """
        path = self.get_path(path_str)
        _date = others.date_format()
        # _log = '[%s]\t[%s] - %s\r\n' % (_date, 'content', str(content))
        if self.print_flag:
            self.log(content)
        if self.save_flag:
            write(path, content, self.max_clear)

    def get_path(self, end_path):
        """
        日志类获取绝对路径
        :param end_path:
        :return:
        """
        _STATIC_TXT = os.path.join('', self.path + end_path)
        return _STATIC_TXT

    def __new__(cls, *args, **kwargs):
        instance = Singleton.createDbOpera(cls)
        return instance
