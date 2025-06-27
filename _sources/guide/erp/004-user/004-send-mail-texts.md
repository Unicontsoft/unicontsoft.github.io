```{only} html
[Нагоре](000-index)
```

# Автоматичен текст при изпращане на e-mail

Настройки на шаблона се намират във файл **EmailTemplate.txt** в папката
на **Dreem.exe** (C:\\Program Files\\Dreem Enterprise 1.5)**.** 

Шаблонът работи със следните променливи:

 - RECIP\_NAME 

 - RECIP\_EMAIL 

 - RECIP\_CC\_NAME 

 - RECIP\_CC\_EMAIL 

 - RECIP\_BCC\_NAME 

 - RECIP\_BCC\_EMAIL 

 - MAIL\_SUBJECT 

 - MAIL\_BODY 

 - CGOWNER\_NAME 

 - PERSON\_NAME 

 - ATTACHMENT\_NAME 

 - ATTACHMENT\_SUFFIX (.PDF по подразбиране) 

 - ATTACHMENT\_TYPE (1 по подразбиране) 

 - TEMP\_FILE 

Съдържание на примерен **EmailTemplate.txt**:

    MAIL_SUBJECT: Прикрепен {ATTACHMENT_NAME} от {CGOWNER_NAME}

    body line 1

    body line 2

    ...

Всяка от променливите може да се употреби в текста във вид
{име-на-променлива} и/или инициализира с нова стойност в
**EmailTemplate.txt** като на отделен ред се сложи

    име-на-променлива: <стойност>

. . . където самата \<стойност\> може да съдържа променливи. Всички останали
редове на шаблона са основен текст (email body).

Валидни стойности за ATTACHMENT\_TYPE:

 - 1 - PDF (по подразбиране)
 - 2 - XLS
 - 3 - MHT
 - 4 - HTML
 - 5 - RTF

Желателно е ATTACHMENT\_SUFFIX да се държи в синхрон с ATTACHMENT\_TYPE,
например

    MAIL_SUBJECT: Електронна фактура {ATTACHMENT_NAME}!

    ATTACHMENT_TYPE: 2

    ATTACHMENT_SUFFIX: .XLS

    body

    ...
