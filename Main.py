#importações de módulos
import os
import win32file
import win32con
import re
from DefineHomePath import in_folder
from AgrupadorArquivos import agrupador
from Analisador import analisador

#verifica modificações na pasta in
ACTIONS = {
  1 : "LIDO: ",
  2 : "REMOVIDO: "
}

FILE_LIST_DIRECTORY = 0x0001

path_to_watch = in_folder
hDir = win32file.CreateFile (
  path_to_watch,
  FILE_LIST_DIRECTORY,
  win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
  None,
  win32con.OPEN_EXISTING,
  win32con.FILE_FLAG_BACKUP_SEMANTICS,
  None
)

while 1:
  results = win32file.ReadDirectoryChangesW (
    hDir,
    8192,
    True,
    win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
    win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
    win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
    win32con.FILE_NOTIFY_CHANGE_SIZE |
    win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
    win32con.FILE_NOTIFY_CHANGE_SECURITY,
    None,
    None
  )
  
  #verifica cada arquivo se a extensão é .dat
  for action, file in results:
    if (action == 1 or action == 2) and re.search('\\.dat', file):
            full_filename = os.path.join(path_to_watch, file)
            print(ACTIONS.get (action, "Acao Desconhecida"), full_filename)
            
            #reune todos os arquivos em uma lista
            verificarFile = agrupador(file)
            
            #analisa a lista e gera o relatório
            analisador(verificarFile)