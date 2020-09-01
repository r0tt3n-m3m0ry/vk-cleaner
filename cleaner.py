try:
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    import vk_api
except:
    print('Установите необходимые модули командой \'$ pip3 install -r requirements.txt\' перед запуском скрипта!')
    exit()

import vk_cleaner_design
import time
import sys


class App(QMainWindow, vk_cleaner_design.Ui_vk_cleaner):
    def __init__(self):
        super().__init__()
        self.ui = vk_cleaner_design.Ui_vk_cleaner()
        self.ui.setupUi(self)
        self.ui.vk_clear.clicked.connect(self.clear_vk_data)

    def clear_vk_data(self):

        while True:
            try:
                vk_session = vk_api.VkApi(QInputDialog.getText(self, 'Auth', 'VK login: ')[0], QInputDialog.getText(self, 'Auth', 'VK password: ')[
                                          0], app_id='2685278', auth_handler=lambda: [QInputDialog.getText(self, 'Two-Factor Auth', 'Two-Factor auth code: '), False])
                vk_session.auth()
                vk = vk_session.get_api()
            except vk_api.exceptions.LoginRequired:
                QMessageBox.about(
                    self, 'Ошибка', 'Логин не может быть пустым!')
            except vk_api.exceptions.PasswordRequired:
                QMessageBox.about(
                    self, 'Ошибка', 'Пароль не может быть пустым!')
            except vk_api.exceptions.BadPassword:
                QMessageBox.about(self, 'Ошибка', 'Неверный пароль!')
            except vk_api.exception.Captcha:
                QMessageBox.about(
                    self, 'Ошибка', 'Превышено максимальное количество запросов за короткое время. Подождите 5 секунд')
            else:
                QMessageBox.about(self, 'Успешно', 'Вы в VK!')
                break

        if self.ui.checkbox_clear_wall.isChecked() == True:
            self.ui.log_browser.append(
                f'Удаляем записи на стене ({vk.wall.get()["count"]})')

            while vk.wall.get(count=100)['count'] != 0:
                for post in vk.wall.get(count=100)['items']:
                    vk.wall.delete(post_id=post['id'])
                    time.sleep(1)

        if self.ui.checkbox_clear_groups.isChecked() == True:
            self.ui.log_browser.append(
                f'Удаляем группы ({vk.groups.get()["count"]})')

            while vk.groups.get(count=1000)['count'] != 0:
                for group in vk.groups.get(count=1000)['items']:
                    vk.groups.leave(group_id=group)
                    time.sleep(1)

        if self.ui.checkbox_clear_messages.isChecked() == True:
            self.ui.log_browser.append(
                f'Удаляем диалоги ({vk.messages.getConversations()["count"]})')

            while vk.messages.getConversations(count=200)['count'] != 0:
                for chat in vk.messages.getConversations(count=200)['items']:
                    vk.messages.deleteConversation(user_id=chat['conversation']['peer']['id'])
                    time.sleep(1)

        if self.ui.checkbox_clear_photos.isChecked() == True:
            self.ui.log_browser.append(
                f'Удаляем фотографии ({vk.photos.getAll(count=100)["count"]})')

            while vk.photos.getAll(count=200)['count'] != 0:
                for photo in vk.photos.getAll(count=200)['items']:
                    vk.photos.delete(photo_id=photo['id'])
                    time.sleep(1)

            while vk.photos.getAlbums()['count'] != 0:
                for album in vk.photos.getAlbums()['items']:
                    vk.photos.deleteAlbum(album_id=album['id'])
                    time.sleep(1)

        if self.ui.checkbox_clear_friends.isChecked() == True:
            self.ui.log_browser.append(
                f'Удаляем друзей ({vk.friends.get()["count"]})')

            while vk.friends.get(count=5000)['count'] != 0:
                for friend in vk.friends.get(count=5000)['items']:
                    vk.friends.delete(user_id=friend)
                    time.sleep(1)

            vk.friends.deleteAllRequests()

            if vk.friends.getLists()['count'] != 0:
                for friends_list in vk.friends.getLists()['items']:
                    vk.friends.deleteList(list_id=friends_list['id'])
                    time.sleep(1)

        if self.ui.checkbox_clear_subscriptions.isChecked() == True:
            self.ui.log_browser.append(
                f'Удаляем подписчиков ({vk.users.getFollowers()["count"]})')

            subs_users = []

            while vk.users.getFollowers(count=1000)['count'] != len(subs_users):
                for users_offset in range(0, vk.users.getFollowers(count=1000)['count'], 1000):
                   for user in vk.users.getFollowers(count=1000, offset=users_offset)['items']:
                        subs_users.append(user['id'])
                   time.sleep(1)

            for user in subs_users:
                vk.account.ban(owner_id=user)
                time.sleep(1)

            time.sleep(1500)

            for user in subs_users:
                vk.account.unban(owner_id=user)
                time.sleep(1)

            del(subs_users)

            self.ui.log_browser.append(
                f'Удаляем подписки на паблики ({vk.users.getSubscriptions()["groups"]["count"]})')

            while vk.users.getSubscriptions(count=200)['groups']['count'] != 0:
                for group in vk.users.getSubscriptions(count=200)['groups']['items']:
                    vk.groups.leave(group_id=group)
                    time.sleep(1)

            self.ui.log_browser.append(
                f'Удаляем подписки на пользователей ({vk.users.getSubscriptions()["users"]["count"]})')

            while vk.users.getSubscriptions(count=200)['users']['count'] != 0:
                for user in vk.users.getSubscriptions(count=200)['users']['items']:
                    vk.friends.delete(user_id=user['id'])
                    time.sleep(1)

        QMessageBox.about(self, 'Успешно', 'Работа программы завершена!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()