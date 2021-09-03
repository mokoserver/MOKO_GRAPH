import MOKO

MOKO.Messenger('set','Приветствие','Рады приветствовать вас на '
                                   'демонстрации приложения MOKO Graph от компании MOKO! Наслаждайтесь!','void', 7)

#Region Status
#hesh done
MOKO.Program('tree', 'set', 'select = ' + 'done')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

MOKO.EndScript()