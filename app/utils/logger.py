import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"


def setup_logger():
    # 防止重复添加handler，导致日志重复
    root_logger = logging.getLogger()
    if root_logger.handlers:
        return

    # 定义日志格式
    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    # 创建console_handler和file_handler
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    # 给两个handler绑定日志格式
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 设置日志等级
    root_logger.setLevel(logging.INFO)

    # 给root_logger添加handler
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
