```{only} html
[Нагоре](000-index)
```

# Референтни номенклатури за ТРЗ

За коректната работа на модул **ТРЗ** е необходимо конфигуриране на някои задължителни параметри.  
Тези настройки се правят предварително в **Референтни номенклатури**. Голяма част от тях са системно въведени и се актуализират автоматично.    

Процесът по добавяне на нова референтна номенклатура е следният:  

1) Избира се група функции **Номенклатури || Референтни номенклатури || ТРЗ**.  
Нова референтна номенклатура се добавя чрез реда за нов запис, стоящ в началото на всеки списък.  
След попълване на всички колони промените трябва да бъдат записани.  

![](901-payroll-settings1.png){ class=align-center w=15cm }

2) **Национална класификация на икономическите дейности** – поле **Код** се попълва, като може да се използва абревиатура на наименованието на дейността. В колона **Национална класификация на икономическите дейности** се посочва основната дейност на предприятието. Попълват се задължително и полета с **Процент трудова злополука** и **От дата**.  
Ако има самоосигуряващи се лица, **Процент трудова злополука** на реда трябва да е **0**. 

3) **Национална класификация на професиите и длъжностите** – в отделни записи се въвеждат всички длъжности и професии, на които има назначени служителите във фирмата, включително самоосигуряващи се лица.  

4) **Категории труд** - за улеснение номенклатурата е системно въведена;  
Основно изискване е да има настроена категорията по подразбиране (според категория труд, отнасяща се до по–голямата част от служителите).  

5) **Минимална работна заплата** - в съответните колони се попълват брутна и нетна минимална РЗ, година и месец, от които са валидни;  

6) **Процент прослужено време** – чрез тази настройка се посочва процент, с който се увеличава РЗ според годините трудов стаж на служителя.  
Попълват се задължително колони **Минимален бр. години стаж** и **Процент**. По желание се попълва колона **Максимален бр. години стаж**.  

7) **Минимален осигурителен праг** - настройката изисква за всяка година да се попълва минимален и максимален осигурителен праг за всяка една от длъжностите във фирмата.  
Полета **Национална класификация на икономическите дейности** и **Национална класификация на професиите и длъжностите** се обзавеждат от падащи списъци, които трябва да са предварително въведени (т.2 и т. 3).  
В номенклатурата се добавя и ред за самоосигуряващи се лица, където **Пореден номер на основната икономическа дейност на осигурителя** е **9999**.  

8) **Данък** - настройката за ДОД изисква въвеждане на отделен ред за всяка година със съответния процент, който се начислява.  
За да се активира ежемесечно начисляване на данък, трябва да се постави отметка в поле **Месечен**.  

9) **Удръжки/Надбавки** - настройката позволява да се въведе списък с различни удръжки и/или надбавки, които да се отнесат по колони от Декларация 1;  
За всяка удръжка/надбавка се поставя отметка в необходимите колони: **Дължат се осигуровки**, **Социален разход**, **Начислява се ДОД**, **% просл. време**, **Следи се в картона на служителя** и **Не е база за изчисление на отпуск**. 

10) **Типове РПВ** - за добавяне на нова номенклатура системата изисква попълване на поле **Код** и  поле с наименование - **Типове РПВ**.  

11) **Кодове за вид плащане** - настройката е системно въведена;  
За добавяне на нов запис се попълват поле **Код** и наименованието му в поле **Кодове за вид плащане**.

12) **Празници и почивни дни** - настройката е системно въведена и включва всички дни за годината, официално приети за неработни;  
Системата дава възможност да се добавят нови записи. Попълват се дата, наименование и в колона **Тип** денят се посочва като *Официален празник* или *Почивен*.  

13) **Вид осигурен** - в тази номенклатура се настройва списък с кодове и вид осигурен според указанията за попълване на Декларация 1.  

14) **Видове документи за отпуск** - системно въведени настройки, включващи необходимите видове документи за отпуск; 

15) **Видове болнични документи** - системно въведени настройки, включващи необходимите видове болнични документи;  

16) **Осигуровки** - системно въведена номенклатура, включваща необходимите настройки за осигуровки;  

17) **Процент на осигуровки** – при тази настройка се въвежда списък с данни за проценти от заплатата, които се начисляват за осигуровки;  
В полета **% за сметка на служителя** и **% за сметка на работодателя** се посочва каква част от съответните осигуровки се разпределят за служител и работодател.  
Настройките се попълват с отделен ред за всяка година.  

18) **Данъчни облекчения за лица с намалена трудоспособност** - при тази настройка се въвежда списък по години с месечната сума на данъчното облекчение;  

19) **Запис** - Бутон в лентата с инструменти, който записва промените.