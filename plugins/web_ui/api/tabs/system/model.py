


from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


class DirFile(BaseModel):

  """
  文件或文件夹
  """

  is_file: bool
  """是否为文件"""
  name: str
  """文件夹或文件名称"""
  parent: Optional[str] = None
  """父级"""

class DeleteFile(BaseModel):

  """
  删除文件
  """

  full_path: str
  """文件全路径"""

class RenameFile(BaseModel):

  """
  删除文件
  """
  parent: Optional[str]
  """父路径"""
  old_name: str
  """旧名称"""
  name: str
  """新名称"""


class AddFile(BaseModel):

  """
  新建文件
  """
  parent: Optional[str]
  """父路径"""
  name: str
  """新名称"""
