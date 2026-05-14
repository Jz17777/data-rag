"""
日志模块 - 基于 loguru 实现

提供三种日志输出：
1. 控制台输出（INFO 级别，带颜色）
2. 应用日志文件（DEBUG 级别，记录所有日志）
3. 错误日志文件（ERROR 级别，只记录错误）
"""

import sys
from pathlib import Path

from loguru import logger

# 日志文件存放目录（项目根目录下的 logs 文件夹）
LOG_DIR = Path(__file__).resolve().parent.parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# 清除 loguru 默认的控制台输出，使用自定义配置
logger.remove()

# 输出到控制台（开发时实时查看）
logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    colorize=True,
)

# 输出到应用日志文件（记录所有级别，用于排查问题）
logger.add(
    LOG_DIR / "app_{time:YYYY-MM-DD}.log",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    rotation="00:00",      # 每天 0 点轮转，生成新文件
    retention="30 days",   # 保留 30 天
    compression="gz",      # 旧日志压缩为 gz 格式
    encoding="utf-8",
)

# 输出到错误日志文件（只记录 ERROR 及以上，快速定位严重问题）
logger.add(
    LOG_DIR / "error_{time:YYYY-MM-DD}.log",
    level="ERROR",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    rotation="00:00",      # 每天 0 点轮转
    retention="60 days",   # 错误日志保留更久（60 天）
    compression="gz",
    encoding="utf-8",
)
