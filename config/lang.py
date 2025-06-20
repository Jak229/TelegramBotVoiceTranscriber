# LANGUAGE SETTINGS

supported_languages = [
    "ru",
    "en",
    "ua",
    "fr",
    "de",
    "it",
    "pl",
    "es",
    "tr",
    "pt",
    "ro",
]  # Supported languages

# Language settings for the bot
LANG = {
    "ru": {
        "start": "<b>Привет, я бот для перевода гс в текст!</b>",
        "help": "Бот для перевода гс в текст.\n"
        "Чтобы начать, выберите язык и отправьте голосовое сообщение.\n"
        "Чтобы выьрать язык, перейдите в меню профиля и выберите язык.\n",
        "lang": "<b>Доступные языки:</b>",
        "no_lang": "<b>Такого языка нет!</b>",
        "change_lang": "Вы изменили язык на {}" "\nЧтобы язык изменился введите /start",
        "error_transcribe": "<b>Ошибка распознавания речи!</b>\n"
        "<b>Проверьте файл на наличие звука или попробуйте другой файл.</b>\n"
        "<b>Если ошибка повторяется, сообщите администратору.</b>",
        "wait_transcribe": "<b>Ждите, идет распознавание...</b>\n"
        "<b>Это может занять некоторое время.</b>\n"
        "<b>Пожалуйста, не отправляйте больше голосовых сообщений.</b>",
        "profile_info": "<b>Профиль</b>\n"
        "<b>ID</b>: {}\n"
        "<b>UserName</b>: <code>@{}</code>\n"
        "<b>Язык</b>: <code>{}</code>\n"
        "<b>Админ</b>: <code>{}</code>",
        "count_users": "<b>Количество пользователей:</b> {}",
        "admin_menu": "<b>Админ меню</b>\n" "<b>Выберите действие:</b>",
        "enter_admin": "<b>Введите ID админа:</b>",
        "success_add_admin": "Администратор успешно добавлен!",
        "success_delete_admin": "Администратор успешно удален!",
        "enter_text": "<b>Введите текст:</b>",
        "has_image": "<b>У вас есть изображение?</b>\n",
        "send_image": "<b>Отправьте изображение:</b>\n",
        "mail_list_end": "<b>Рассылка завершена!</b>\n"
        "<b>Отправлено сообщений:</b> {}\n"
        "<b>Ошибок: </b> {}",
        "flood": "<b>Вы отправили слишком много сообщений!</b>\n",
    },
    "en": {
        "start": "<b>Hello, I am a bot for translating gs into text!</b>",
        "help": "Bot for translating voice message into text.\n"
        "To get started, select a language and send a voice message.\n"
        "To choose a language, go to the profile menu and select a language.\n",
        "lang": "Choose a language:",
        "no_lang": "<b>This language does not exist!</b>",
        "change_lang": "You have changed the language to {}"
        "\nTo change the language, enter /start",
        "error_transcribe": "<b>Speech recognition error!</b>\n"
        "<b>Check the file for sound or try another file.</b>\n"
        "<b>If the error persists, please contact the administrator.</b>",
        "wait_transcribe": "<b>Please wait, recognition is in progress...</b>\n"
        "<b>This may take some time.</b>\n"
        "<b>Please do not send more voice messages.</b>",
        "profile_info": "<b>Profile</b>\n"
        "<b>ID</b>: {}\n"
        "<b>UserName</b>: <code>@{}</code>\n"
        "<b>Language</b>: <code>{}</code>\n"
        "<b>Admin</b>: <code>{}</code>",
        "count_users": "<b>Number of users:</b> {}",
        "admin_menu": "<b>Admin menu</b>\n" "<b>Select an action:</b>",
        "enter_admin": "<b>Enter admin ID:</b>",
        "success_add_admin": "Admin added successfully!",
        "success_delete_admin": "Admin deleted successfully!",
        "enter_text": "<b>Enter text:</b>",
        "has_image": "<b>Do you have an image?</b>\n",
        "send_image": "<b>Send image:</b>\n",
        "mail_list_end": "<b>Mailing list completed!</b>\n"
        "<b>Messages sent:</b> {}\n"
        "<b>Errors: </b> {}",
        "flood": "<b>You have sent too many messages!</b>\n",
    },
    "ua": {
        "start": "<b>Привіт, я бот для перекладу гс в текст!</b>",
        "help": "Бот для перекладу гс в текст.\n"
        "Щоб почати, виберіть мову та надішліть голосове повідомлення.\n"
        "Щоб вибрати мову, перейдіть у меню профілю та виберіть мову.\n",
        "lang": "<b>Доступні мови:</b>",
        "no_lang": "<b>Такої мови немає!</b>",
        "change_lang": "Ви змінили мову на {}\n" "Щоб мова змінилася введіть /start",
        "error_transcribe": "<b>Помилка розпізнавання мови!</b>\n"
        "<b>Перевірте файл на наявність звуку або спробуйте інший файл.</b>\n"
        "<b>Якщо помилка повторюється, повідомте адміністратору.</b>",
        "wait_transcribe": "<b>Чекайте, йде розпізнавання...</b>\n"
        "<b>Це може зайняти деякий час.</b>\n"
        "<b>Будь ласка, не надсилайте більше голосових повідомлень.</b>",
        "profile_info": "<b>Профіль</b>\n"
        "<b>ID</b>: {}\n"
        "<b>UserName</b>: <code>@{}</code>\n"
        "<b>Мова</b>: <code>{}</code>\n"
        "<b>Адмін</b>: <code>{}</code>",
        "count_users": "<b>Кількість користувачів:</b> {}",
        "admin_menu": "<b>Адмін меню</b>\n" "<b>Виберіть дію:</b>",
        "enter_admin": "<b>Введіть ID адміна:</b>",
        "success_add_admin": "Адміністратор успішно доданий!",
        "success_delete_admin": "Адміністратор успішно видалений!",
        "enter_text": "<b>Введіть текст:</b>",
        "has_image": "<b>У вас є зображення?</b>\n",
        "send_image": "<b>Надішліть зображення:</b>\n",
        "mail_list_end": "<b>Розсилка завершена!</b>\n"
        "<b>Повідомлень надіслано:</b> {}\n"
        "<b>Помилок: </b> {}",
        "flood": "<b>Ви надіслали занадто багато повідомлень!</b>\n",
    },
    "fr": {
        "start": "<b>Bonjour, je suis un bot pour traduire gs en texte!</b>",
        "help": "Bot pour traduire le message vocal en texte.\n"
        "Pour commencer, sélectionnez une langue et envoyez un message vocal.\n"
        "Pour choisir une langue, allez dans le menu de profil et sélectionnez une langue.\n",
        "lang": "Choisissez une langue:",
        "no_lang": "<b>Cette langue n'existe pas!</b>",
        "change_lang": "Vous avez changé la langue en {}"
        "\nPour changer la langue, entrez /start",
        "error_transcribe": "<b>Erreur de reconnaissance vocale!</b>\n"
        "<b>Vérifiez le fichier pour le son ou essayez un autre fichier.</b>\n"
        "<b>Si l'erreur persiste, veuillez contacter l'administrateur.</b>",
        "wait_transcribe": "<b>Veuillez patienter, la reconnaissance est en cours...</b>\n"
        "<b>Cela peut prendre un certain temps.</b>\n"
        "<b>Veuillez ne pas envoyer plus de messages vocaux.</b>",
        "profile_info": "<b>Profil</b>\n"
        "<b>ID</b>: {}\n"
        "<b>UserName</b>: <code>@{}</code>\n"
        "<b>Langue</b>: <code>{}</code>\n"
        "<b>Admin</b>: <code>{}</code>",
        "count_users": "<b>Nombre d'utilisateurs:</b> {}",
        "admin_menu": "<b>Menu admin</b>\n" "<b>Sélectionnez une action:</b>",
        "enter_admin": "<b>Entrez l'ID de l'administrateur:</b>",
        "success_add_admin": "Administrateur ajouté avec succès!",
        "success_delete_admin": "Administrateur supprimé avec succès!",
        "enter_text": "<b>Entrez le texte:</b>",
        "has_image": "<b>Avez-vous une image?</b>\n",
        "send_image": "<b>Envoyez l'image:</b>\n",
        "mail_list_end": "<b>Liste de diffusion terminée!</b>\n"
        "<b>Messages envoyés:</b> {}\n"
        "<b>Erreurs: </b> {}",
        "flood": "<b>Vous avez envoyé trop de messages!</b>\n",
    },
    "de": {
        "start": "<b>Hallo, ich bin ein Bot, um gs in Text zu übersetzen!</b>",
        "help": "Bot zum Übersetzen von Sprachnachrichten in Text.\n"
        "Um zu beginnen, wählen Sie eine Sprache und senden Sie eine Sprachnachricht.\n"
        "Um eine Sprache auszuwählen, gehen Sie zum Profilmenü und wählen Sie eine Sprache aus.\n",
        "lang": "Wählen Sie eine Sprache:",
        "no_lang": "<b>Diese Sprache existiert nicht!</b>",
        "change_lang": "Sie haben die Sprache auf {} geändert"
        "\nUm die Sprache zu ändern, geben Sie /start ein",
        "error_transcribe": "<b>Fehler bei der Spracherkennung!</b>\n"
        "<b>Überprüfen Sie die Datei auf Ton oder versuchen Sie eine andere Datei.</b>\n"
        "<b>Wenn der Fehler weiterhin besteht, wenden Sie sich bitte an den Administrator.</b>",
        "wait_transcribe": "<b>Bitte warten, die Erkennung läuft...</b>\n"
        "<b>Dies kann einige Zeit in Anspruch nehmen.</b>\n"
        "<b>Bitte senden Sie keine weiteren Sprachnachrichten.</b>",
        "profile_info": "<b>Profil</b>\n"
        "<b>ID</b>: {}\n"
        "<b>UserName</b>: <code>@{}</code>\n"
        "<b>Sprache</b>: <code>{}</code>\n"
        "<b>Admin</b>: <code>{}</code>",
        "count_users": "<b>Anzahl der Benutzer:</b> {}",
        "admin_menu": "<b>Admin-Menü</b>\n" "<b>Wählen Sie eine Aktion:</b>",
        "enter_admin": "<b>Geben Sie die Admin-ID ein:</b>",
        "success_add_admin": "Admin erfolgreich hinzugefügt!",
        "success_delete_admin": "Admin erfolgreich gelöscht!",
        "enter_text": "<b>Geben Sie den Text ein:</b>",
        "has_image": "<b>Haben Sie ein Bild?</b>\n",
        "send_image": "<b>Bild senden:</b>\n",
        "mail_list_end": "<b>Mailing abgeschlossen!</b>\n"
        "<b>Gesendete Nachrichten:</b> {}\n"
        "<b>Fehler: </b> {}",
        "flood": "<b>Sie haben zu viele Nachrichten gesendet!</b>\n",
    },
    "it": {
        "start": "<b>Ciao, sono un bot per tradurre gs in testo!</b>",
        "help": "Bot per tradurre il messaggio vocale in testo.\n"
        "Per iniziare, seleziona una lingua e invia un messaggio vocale.\n"
        "Per scegliere una lingua, vai nel menu del profilo e seleziona una lingua.\n",
        "lang": "Scegli una lingua:",
        "no_lang": "<b>Questa lingua non esiste!</b>",
        "change_lang": "Hai cambiato la lingua in {}"
        "\nPer cambiare la lingua, inserisci /start",
        "error_transcribe": "<b>Errore di riconoscimento vocale!</b>\n"
        "<b>Controlla il file per il suono o prova un altro file.</b>\n"
        "<b>Se l'errore persiste, contatta l'amministratore.</b>",
        "wait_transcribe": "<b>Attendere, il riconoscimento è in corso...</b>\n"
        "<b>Questo potrebbe richiedere del tempo.</b>\n"
        "<b>Si prega di non inviare più messaggi vocali.</b>",
        "profile_info": "<b>Profilo</b>\n"
        "<b>ID</b>: {}\n"
        "<b>UserName</b>: <code>@{}</code>\n"
        "<b>Lingua</b>: <code>{}</code>\n"
        "<b>Admin</b>: <code>{}</code>",
        "count_users": "<b>Numero di utenti:</b> {}",
        "admin_menu": "<b>Menu admin</b>\n" "<b>Seleziona un'azione:</b>",
        "enter_admin": "<b>Inserisci l'ID dell'amministratore:</b>",
        "success_add_admin": "Amministratore aggiunto con successo!",
        "success_delete_admin": "Amministratore eliminato con successo!",
        "enter_text": "<b>Inserisci il testo:</b>",
        "has_image": "<b>Hai un'immagine?</b>\n",
        "send_image": "<b>Invia immagine:</b>\n",
        "mail_list_end": "<b>Mailing completato!</b>\n"
        "<b>Messaggi inviati:</b> {}\n"
        "<b>Errore: </b> {}",
        "flood": "<b>Hai inviato troppi messaggi!</b>\n",
    },
    "pl": {
        "start": "<b>Cześć, jestem botem do tłumaczenia gs na tekst!</b>",
        "help": "Bot do tłumaczenia wiadomości głosowych na tekst.\n"
        "Aby rozpocząć, wybierz język i wyślij wiadomość głosową.\n"
        "Aby wybrać język, przejdź do menu profilu i wybierz język.\n",
        "lang": "Wybierz język:",
        "no_lang": "<b>Taki język nie istnieje!</b>",
        "change_lang": "Zmieniłeś język na {}" "\nAby zmienić język, wpisz /start",
        "error_transcribe": "<b>Błąd rozpoznawania mowy!</b>\n"
        "<b>Sprawdź plik pod kątem dźwięku lub spróbuj innego pliku.</b>\n"
        "<b>Jeśli błąd się powtarza, skontaktuj się z administratorem.</b>",
        "wait_transcribe": "<b>Proszę czekać, trwa rozpoznawanie...</b>\n"
        "<b>To może zająć trochę czasu.</b>\n"
        "<b>Proszę nie wysyłać więcej wiadomości głosowych.</b>",
        "profile_info": "<b>Profil</b>\n"
        "<b>ID</b>: {}\n"
        "<b>UserName</b>: <code>@{}</code>\n"
        "<b>Język</b>: <code>{}</code>\n"
        "<b>Admin</b>: <code>{}</code>",
        "count_users": "<b>Liczba użytkowników:</b> {}",
        "admin_menu": "<b>Menu admina</b>\n" "<b>Wybierz akcję:</b>",
        "enter_admin": "<b>Wprowadź ID administratora:</b>",
        "success_add_admin": "Administrator pomyślnie dodany!",
        "success_delete_admin": "Administrator pomyślnie usunięty!",
        "enter_text": "<b>Wprowadź tekst:</b>",
        "has_image": "<b>Czy masz obrazek?</b>\n",
        "send_image": "<b>Wyślij obrazek:</b>\n",
        "mail_list_end": "<b>Mailing zakończony!</b>\n"
        "<b>Wysłane wiadomości:</b> {}\n"
        "<b>Błędy: </b> {}",
        "flood": "<b>Wysłałeś za dużo wiadomości!</b>\n",
    },
    "es": {
        "start": "<b>Hola, soy un bot para traducir gs a texto!</b>",
        "help": "Bot para traducir el mensaje de voz en texto.\n"
        "Para empezar, selecciona un idioma y envía un mensaje de voz.\n"
        "Para elegir un idioma, ve al menú de perfil y selecciona un idioma.\n",
        "lang": "Elige un idioma:",
        "no_lang": "<b>¡Este idioma no existe!</b>",
        "change_lang": "Has cambiado el idioma a {}"
        "\nPara cambiar el idioma, ingresa /start",
        "error_transcribe": "<b>¡Error de reconocimiento de voz!</b>\n"
        "<b>Verifica el archivo por sonido o prueba otro archivo.</b>\n"
        "<b>Si el error persiste, comunícate con el administrador.</b>",
        "wait_transcribe": "<b>Por favor espera, el reconocimiento está en progreso...</b>\n"
        "<b>Esto puede tardar un tiempo.</b>\n"
        "<b>Por favor no envíes más mensajes de voz.</b>",
        "profile_info": "<b>Perfil</b>\n"
        "<b>ID</b>: {}\n"
        "<b>UserName</b>: <code>@{}</code>\n"
        "<b>Idioma</b>: <code>{}</code>\n"
        "<b>Admin</b>: <code>{}</code>",
        "count_users": "<b>Número de usuarios:</b> {}",
        "admin_menu": "<b>Menú de administrador</b>\n" "<b>Selecciona una acción:</b>",
        "enter_admin": "<b>Ingresa el ID del administrador:</b>",
        "success_add_admin": "¡Administrador agregado con éxito!",
        "success_delete_admin": "¡Administrador eliminado con éxito!",
        "enter_text": "<b>Ingresa el texto:</b>",
        "has_image": "<b>¿Tienes una imagen?</b>\n",
        "send_image": "<b>Enviar imagen:</b>\n",
        "mail_list_end": "<b>¡Lista de correo completada!</b>\n"
        "<b>Mensajes enviados:</b> {}\n"
        "<b>Errores: </b> {}",
        "flood": "<b>¡Has enviado demasiados mensajes!</b>\n",
    },
    "tr": {
        "start": "<b>Merhaba, ben gs'yi metne çeviren bir botum!</b>",
        "help": "Sesli mesajı metne çeviren bot.\n"
        "Başlamak için bir dil seçin ve sesli mesaj gönderin.\n"
        "Bir dil seçmek için profil menüsüne gidin ve bir dil seçin.\n",
        "lang": "Bir dil seçin:",
        "no_lang": "<b>Bu dil yok!</b>",
        "change_lang": "Dili {} olarak değiştirdiniz"
        "\nDili değiştirmek için /start yazın",
        "error_transcribe": "<b>Ses tanıma hatası!</b>\n"
        "<b>Dosyayı ses için kontrol edin veya başka bir dosya deneyin.</b>\n"
        "<b>Hata devam ederse, lütfen yöneticinizle iletişime geçin.</b>",
        "wait_transcribe": "<b>Lütfen bekleyin, tanıma devam ediyor...</b>\n"
        "<b>Bu biraz zaman alabilir.</b>\n"
        "<b>Lütfen daha fazla sesli mesaj göndermeyin.</b>",
        "profile_info": "<b>Profil</b>\n"
        "<b>ID</b>: {}\n"
        "<b>Kullanıcı Adı</b>: <code>@{}</code>\n"
        "<b>Dil</b>: <code>{}</code>\n"
        "<b>Yönetici</b>: <code>{}</code>",
        "count_users": "<b>Kullanıcıların sayısı:</b> {}",
        "admin_menu": "<b>Yönetici menüsü</b>\n" "<b>Bir eylem seçin:</b>",
        "enter_admin": "<b>Yönetici kimliğini girin:</b>",
        "success_add_admin": "Yönetici başarıyla eklendi!",
        "success_delete_admin": "Yönetici başarıyla silindi!",
        "enter_text": "<b>Metni girin:</b>",
        "has_image": "<b>Bir resminiz var mı?</b>\n",
        "send_image": "<b>Resmi gönder:</b>\n",
        "mail_list_end": "<b>Posta listesi tamamlandı!</b>\n"
        "<b>Gönderilen mesajlar:</b> {}\n"
        "<b>Hatalar: </b> {}",
        "flood": "<b>Çok fazla mesaj gönderdiniz!</b>\n",
    },
        "pt": {
        "start": "<b>Olá, sou um bot para traduzir gs em texto!</b>",
        "help": "Bot para traduzir a mensagem de voz em texto.\n"
        "Para começar, selecione um idioma e envie uma mensagem de voz.\n"
        "Para escolher um idioma, vá para o menu de perfil e selecione um idioma.\n",
        "lang": "Escolha um idioma:",
        "no_lang": "<b>Este idioma não existe!</b>",
        "change_lang": "Você mudou o idioma para {}"
        "\nPara mudar o idioma, digite /start",
        "error_transcribe": "<b>Erro de reconhecimento de fala!</b>\n"
        "<b>Verifique o arquivo para som ou tente outro arquivo.</b>\n"
        "<b>Se o erro persistir, entre em contato com o administrador.</b>",
        "wait_transcribe": "<b>Por favor, aguarde, o reconhecimento está em andamento...</b>\n"
        "<b>Isto pode levar algum tempo.</b>\n"
        "<b>Por favor, não envie mais mensagens de voz.</b>",
        "profile_info": "<b>Perfil</b>\n"
        "<b>ID</b>: {}\n"
        "<b>Nome de usuário</b>: <code>@{}</code>\n"
        "<b>Idioma</b>: <code>{}</code>\n"
        "<b>Admin</b>: <code>{}</code>",
        "count_users": "<b>Número de usuários:</b> {}",
        "admin_menu": "<b>Menu do administrador</b>\n" "<b>Selecione uma ação:</b>",
        "enter_admin": "<b>Digite o ID do administrador:</b>",
        "success_add_admin": "Administrador adicionado com sucesso!",
        "success_delete_admin": "Administrador excluído com sucesso!",
        "enter_text": "<b>Digite o texto:</b>",
        "has_image": "<b>Você tem uma imagem?</b>\n",
        "send_image": "<b>Enviar imagem:</b>\n",
        "mail_list_end": "<b>Lista de mala direta concluída!</b>\n"
        "<b>Mensagens enviadas:</b> {}\n"
        "<b>Erros: </b> {}",
        "flood": "<b>Você enviou muitas mensagens!</b>\n",
    },
    "ro": {
        "start": "<b>Bună, sunt un bot pentru a traduce gs în text!</b>",
        "help": "Bot pentru a traduce mesajul vocal în text.\n"
        "Pentru a începe, selectați o limbă și trimiteți un mesaj vocal.\n"
        "Pentru a alege o limbă, mergeți la meniul de profil și selectați o limbă.\n",
        "lang": "Alegeți o limbă:",
        "no_lang": "<b>Această limbă nu există!</b>",
        "change_lang": "Ați schimbat limba în {}"
        "\nPentru a schimba limba, introduceți /start",
        "error_transcribe": "<b>Eroare de recunoaștere vocală!</b>\n"
        "<b>Verificați fișierul pentru sunet sau încercați un alt fișier.</b>\n"
        "<b>Dacă eroarea persistă, vă rugăm să contactați administratorul.</b>",
        "wait_transcribe": "<b>Vă rugăm să așteptați, recunoașterea este în curs de desfășurare...</b>\n"
        "<b>Asta poate dura ceva timp.</b>\n"
        "<b>Vă rugăm să nu trimiteți mai multe mesaje vocale.</b>",
        "profile_info": "<b>Profil</b>\n"
        "<b>ID</b>: {}\n"
        "<b>Nume de utilizator</b>: <code>@{}</code>\n"
        "<b>Limbă</b>: <code>{}</code>\n"
        "<b>Admin</b>: <code>{}</code>",
        "count_users": "<b>Numărul de utilizatori:</b> {}",
        "admin_menu": "<b>Meniul administratorului</b>\n" "<b>Selectați o acțiune:</b>",
        "enter_admin": "<b>Introduceți ID-ul administratorului:</b>",
        "success_add_admin": "Administrator adăugat cu succes!",
        "success_delete_admin": "Administrator șters cu succes!",
        "enter_text": "<b>Introduceți textul:</b>",
        "has_image": "<b>Ai o imagine?</b>\n",
        "send_image": "<b>Trimiteți imaginea:</b>\n",
        "mail_list_end": "<b>Lista de corespondență finalizată!</b>\n"
        "<b>Mesaje trimise:</b> {}\n"
        "<b>Erori: </b> {}",
        "flood": "<b>Ați trimis prea multe mesaje!</b>\n",
    },
}

# Button texts for different languages
KEY_LANG = {
    "ru": {
        "profile": "Профиль",
        "info": "Информация",
        "help": "Помощь",
        "language": "Язык",
        "back": "Назад",
        "admin_menu": "Админ меню",
        "cancel": "Отмена",
        "admin": "Админ",
        "channel": "Канал",
        "add_admin": "Добавить админа",
        "delete_admin": "Удалить админа",
        "mailing_list": "Рассылка",
        "has": "Есть",
        "no": "Нет",
        "send": "Отправить",
        "cancel": "Отмена",
    },
    "en": {
        "profile": "Profile",
        "info": "Information",
        "help": "Help",
        "language": "Language",
        "back": "Back",
        "admin_menu": "Admin menu",
        "cancel": "Cancel",
        "admin": "Admin",
        "channel": "Channel",
        "add_admin": "Add admin",
        "delete_admin": "Delete admin",
        "mailing_list": "Mailing list",
        "has": "Has",
        "no": "No",
        "send": "Send",
        "cancel": "Cancel",
    },
    "ua": {
        "profile": "Профіль",
        "info": "Інформація",
        "help": "Допомога",
        "language": "Мова",
        "back": "Назад",
        "admin_menu": "Адмін меню",
        "cancel": "Відміна",
        "admin": "Адмін",
        "channel": "Канал",
        "add_admin": "Додати адміна",
        "delete_admin": "Видалити адміна",
        "mailing_list": "Розсилка",
        "has": "Є",
        "no": "Немає",
        "send": "Відправити",
        "cancel": "Відміна",
    },
    "fr": {
        "profile": "Profil",
        "info": "Information",
        "help": "Aide",
        "language": "Langue",
        "back": "Retour",
        "admin_menu": "Menu admin",
        "cancel": "Annuler",
        "admin": "Admin",
        "channel": "Canal",
        "add_admin": "Ajouter admin",
        "delete_admin": "Supprimer admin",
        "mailing_list": "Liste de diffusion",
        "has": "A",
        "no": "Non",
        "send": "Envoyer",
        "cancel": "Annuler",
    },
    "de": {
        "profile": "Profil",
        "info": "Information",
        "help": "Hilfe",
        "language": "Sprache",
        "back": "Zurück",
        "admin_menu": "Admin-Menü",
        "cancel": "Abbrechen",
        "admin": "Admin",
        "channel": "Kanal",
        "add_admin": "Admin hinzufügen",
        "delete_admin": "Admin löschen",
        "mailing_list": "Mailingliste",
        "has": "Hat",
        "no": "Nein",
        "send": "Senden",
        "cancel": "Abbrechen",
    },
    "it": {
        "profile": "Profilo",
        "info": "Informazioni",
        "help": "Aiuto",
        "language": "Lingua",
        "back": "Indietro",
        "admin_menu": "Menu admin",
        "cancel": "Annulla",
        "admin": "Admin",
        "channel": "Canale",
        "add_admin": "Aggiungi admin",
        "delete_admin": "Elimina admin",
        "mailing_list": "Lista di distribuzione",
        "has": "Ha",
        "no": "No",
        "send": "Invia",
        "cancel": "Annulla",
    },
    "pl": {
        "profile": "Profil",
        "info": "Informacje",
        "help": "Pomoc",
        "language": "Język",
        "back": "Wstecz",
        "admin_menu": "Menu admina",
        "cancel": "Anuluj",
        "admin": "Admin",
        "channel": "Kanał",
        "add_admin": "Dodaj admina",
        "delete_admin": "Usuń admina",
        "mailing_list": "Lista mailingowa",
        "has": "Ma",
        "no": "Nie",
        "send": "Wyślij",
        "cancel": "Anuluj",
    },
    "es": {
        "profile": "Perfil",
        "info": "Información",
        "help": "Ayuda",
        "language": "Idioma",
        "back": "Atrás",
        "admin_menu": "Menú de administrador",
        "cancel": "Cancelar",
        "admin": "Admin",
        "channel": "Canal",
        "add_admin": "Agregar admin",
        "delete_admin": "Eliminar admin",
        "mailing_list": "Lista de correo",
        "has": "Tiene",
        "no": "No",
        "send": "Enviar",
        "cancel": "Cancelar",
    },
    "tr": {
        "profile": "Profil",
        "info": "Bilgi",
        "help": "Yardım",
        "language": "Dil",
        "back": "Geri",
        "admin_menu": "Yönetici menüsü",
        "cancel": "İptal",
        "admin": "Admin",
        "channel": "Kanal",
        "add_admin": "Admin ekle",
        "delete_admin": "Admin sil",
        "mailing_list": "Posta listesi",
        "has": "Var",
        "no": "Hayır",
        "send": "Gönder",
        "cancel": "İptal",
    },
    "pt": {
        "profile": "Perfil",
        "info": "Informação",
        "help": "Ajuda",
        "language": "Língua",
        "back": "Voltar",
        "admin_menu": "Menu do administrador",
        "cancel": "Cancelar",
        "admin": "Admin",
        "channel": "Canal",
        "add_admin": "Adicionar admin",
        "delete_admin": "Excluir admin",
        "mailing_list": "Lista de mala direta",
        "has": "Tem",
        "no": "Não",
        "send": "Enviar",
        "cancel": "Cancelar",
    },
    "ro": {
        "profile": "Profil",
        "info": "Informație",
        "help": "Ajutor",
        "language": "Limbă",
        "back": "Înapoi",
        "admin_menu": "Meniul administratorului",
        "cancel": "Anulare",
        "admin": "Admin",
        "channel": "Canal",
        "add_admin": "Adaugă admin",
        "delete_admin": "Șterge admin",
        "mailing_list": "Listă de corespondență",
        "has": "Are",
        "no": "Nu",
        "send": "Trimite",
        "cancel": "Anulare",
    },
}
