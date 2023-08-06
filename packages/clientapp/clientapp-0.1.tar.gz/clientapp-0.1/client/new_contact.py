import sys
import logging

sys.path.append('../')
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

LOGGER = logging.getLogger('client')


class AddContactDialog(QDialog):
    '''
    Добавление пользователя в список контактов.
    Предоставляет текщий список пользователей и
    добавляет выбранного в список контактов пользователя.
    '''
    def __init__(self, transport, database):
        super().__init__()
        self.transport = transport
        self.database = database

        self.setFixedSize(350, 120)
        self.setWindowTitle('Выберите контакт для добавления:')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        self.selector_label = QLabel('Выберите контакт для добавления:', self)
        self.selector_label.setFixedSize(200, 20)
        self.selector_label.move(10, 0)

        self.selector = QComboBox(self)
        self.selector.setFixedSize(200, 20)
        self.selector.move(10, 30)

        self.btn_refresh = QPushButton('Обновить список', self)
        self.btn_refresh.setFixedSize(100, 30)
        self.btn_refresh.move(60, 60)

        self.btn_ok = QPushButton('Добавить', self)
        self.btn_ok.setFixedSize(100, 30)
        self.btn_ok.move(230, 20)

        self.btn_cancel = QPushButton('Отмена', self)
        self.btn_cancel.setFixedSize(100, 30)
        self.btn_cancel.move(230, 60)
        self.btn_cancel.clicked.connect(self.close)
        self.possible_contacts_upd()
        self.btn_refresh.clicked.connect(self.upd_possible_contacts)

    def possible_contacts_upd(self):
        '''
        Заполнение списка возможных контактов.
        Создаёт список всех пользователей,
        исключая уже добавленных и самого себя.
        '''
        self.selector.clear()
        contacts_list = set(self.database.get_contacts())
        users_list = set(self.database.get_users())
        users_list.remove(self.transport.username)
        self.selector.addItems(users_list - contacts_list)

    def upd_possible_contacts(self):
        '''
        Обновление списка пользователей доступных для добавления
        в список контактов. Запрашивает с сервера список известных
        пользователей и обносляет содержимое окна.
        '''
        try:
            self.transport.user_list_upd()
        except OSError:
            pass
        else:
            LOGGER.debug('Обновление списка пользователей с сервера выполнено')
            self.possible_contacts_upd()
