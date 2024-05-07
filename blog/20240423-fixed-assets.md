```{only} html
[Нагоре](000-index)
```
 
# Дълготрайни активи

- [Настройки на дълготрайни активи](https://docs.unicontsoft.com/blog/20240423-fixed-assets.html#id2)  
- [Амортизация на дълготрайни активи](https://docs.unicontsoft.com/blog/20240423-fixed-assets.html#id3)  

## Настройки

**Дълготрайни активи** е отделна номенклатура, която системата третира аналогично на **Продукти и материали** и затова попадат в общ списък. Така, въпреки специфичните си настройки, активите може да се използват в документите за покупка и продажба.  
При [въвеждането на ДА](https://www.unicontsoft.com/cms/node/100) системата изисква някои задължителни реквизити, отбелязани с червен маркер. Такива са наименование на *ДА*, стойност и дата на придобиване, дата на въвеждане в експлоатация, счетоводна група и категория(по чл. 55 от ЗКПО).

Счетоводни групи, методи за амортизация, коефициент на преоценка и категории по чл.55 (ЗКПО) могат да бъдат въведени и редактирани от **Номенклатури || Референтни номенклатури || Дълготрайни активи**. Тези настрийки са базови за *ДА* и трябва да се направят преди създаването на нов актив.  
Ако все още не сте направили настройките, темата [Как да въведем Групи ДА](https://www.unicontsoft.com/cms/node/152) ще е полезна. По описания в нея начин се въвеждат и останалите базови за *ДА* настройки.  

Нека въведем в системата един примерен актив - *Лек автомобил*, който попада в *Категория V* с амортизационната норма 25% на година.  
Автомобилът е закупен на 23.04.2024 г. за 39'000 лв. и ще бъде въведен в експлоатация на 01.05.2024 г.

![](20240423-fixed-assets1.png){ class=align-center }

> Препоръчително е да запишете въведените до момента данни, преди да продължите с настройките.

В **Допълнителни** системата е попълнила автоматично задължителните полета, свързани с данъчния и със счетоводния амортизационен план.  
Тук може да добавите също сума за неамортизируемата остатъчна стойност на *ДА*.  

```{tip}
За *ДА* могат да се настроят също и различни дименсии, както е при *Продукти и материали*.
```

![](20240423-fixed-assets2.png){ class=align-center }

На третия панел **Списъци** ще откриете настройки, касаещи подобренията, консервациите и амортизационните норми и план на *ДА*.  
Докато първите две са възможни при определени обстоятелства, то амортизацията е неизбежна след пускане на актива в експлоатация.  
Затова следва да направите нужните настройки за амортизационни норми и амортизационен план.  

Използвайки бутона *Генериране* в лентата с инструменти ще изберете амортизационна норма(или период на експлоатация) и метод на амортизация. 

![](20240423-fixed-assets3.png){ class=align-center }

Системата предлага по подразбиране *Линеен метод* на амортизация. При него годишните амортизационни квоти са еднакви за целия амортизационен период.  
За генерацията на амортизационен план трябва да попълните или поле *Период на експлоатация*, или *Амортизационна норма*. След което потвърждавате избора и записвате промените.

![](20240423-fixed-assets4.png){ class=align-center }
 
Вече може да разгледате генерираните примерни амортизационни планове за този *ДА* - данъчен и счетоводен.

![](20240423-fixed-assets5.png){ class=align-center }

```{tip}
Ако пожелаете да редактирате амортизационните норми в избран *ДА*, респ. амортизационния му план, може да повторите описаната вече генерация.
```

Системата дава възможност за избор от следните методи на амортизация: 
 
- *Константно дегресивен метод* със снижаващ се остатък. 
- Споменатият вече *Линеен метод* с годишните амортизационни квоти, които са еднакви за целия амортизационен период.  
- *Метод на сумата на числата*  
- *Неравномерно дегресивен метод*  
- *Прогресивен нелинеен метод*  
- *Произволен метод*  

## Амортизация на *ДА* - справки и генерация на счетоводни документи

Генерираните в системата амортизационни планове могат да бъдат видени отделно за всеки актив. Както споменахме, това става във формата за редакция на избрания *ДА*.  
Също така има и справка, включваща всички активи, достъпна в **Счетоводство || Печат на амортизационен план*.  
Във филтъра може да изберете вида и типа на амортизационния план, период и други.

![](20240423-fixed-assets6.png){ class=align-center }

Справката, която се зарежда според настроените филтри, включва всички *ДА* със състояние *Активен*.

![](20240423-fixed-assets7.png){ class=align-center }

> Системата разполага с инструмент за автоматична генерация на счетоводни документи с предложените амортизационни квоти.
> Намира се в меню **Счетоводство | Генерация на ДА**.

За да бъдат създадени счетоводни записвания за всички активни *ДА*, трябва да потвърдите желания период.  
Ако поставите отметка за *Приключване*, системата ще валидира счетоводните документи. Пропуснете тази настройка, ако предпочитате да приключите документите ръчно, след като сте проверили тяхното съдържание.

![](20240423-fixed-assets8.png){ class=align-center }

По този начин в меню **Счетоводство || Счетоводни документи** са генерирани по месеци документи от тип **АмПл**.  
От момента на приключването им, данните в тях ще бъдат видими в счетоводните справки.

![](20240423-fixed-assets9.png){ class=align-center }


