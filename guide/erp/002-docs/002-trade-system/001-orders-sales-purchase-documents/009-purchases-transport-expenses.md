```{only} html
[Нагоре](000-index)
```

# Разпределяне на разходи за придобиване

Системата разполага с инструмент за разпределяне на разходи по покупки (за транспорт, за опаковка и др.) и следене на реалната себестойност на продукти и материали.

Процесът по разпределяне на разходи по покупка е следният:  

1) Предварително в системата трябва да се валидират вътрешнофирмените документи за покупката на стоки: **Покупка** и свързан **ПСД**-Приходен складов документ.

2) Въвежда се нов документ за покупка, който включва направените разходи.  
За различните разходи се създават отделни продукти от тип услуга в **Номенклатури || Продукти и материали**.  

3) От меню **Средства || Разпределение на разходи за придобиване** се отваря форма за избор на свързани документи.  

![](909-purchases-transport-expenses1.png){ class=align-center w=15cm }

4) На този етап форма **Разпределение на разходи за придобиване** съдържа единствено ред с разходите за разпределяне от текущата покупка.  
С десен бутон върху реда се избира **Добавяне на редове от ПСД**.  
Отваря се форма за избор **Складови документи**, чрез която трябва да се добавят продуктите, върху чиято стойност се разпределя сумата на разходите.   

> Сума на разходите за разпределяне е винаги без ДДС.

![](909-purchases-transport-expenses2.png){ class=align-center w=15cm }

Отварят се списъци със складови документи и документи за покупка.  
По избор се работи в един от двата списъка.  
Трябва да се посочи или документ за покупката на стоки, или приходният складов документ, към който се отнасят текущите разходи.  
    - с бутон **Напред** - маркира се един или няколко документа **ПСД**/**Покупка** и с бутон **Напред** се продължава към следваща стъпка;  
    - с бутон **Избор** - маркира се един, няколко или всички продукти, върху които да се разпределят разходите и бутон **Избор** ги добавя в списъка на формата за разпределение;    

![](909-purchases-transport-expenses3.png){ class=align-center w=15cm }

- **Ред от свързан документ** -  по редовете в колоната се виждат всички разходи по придобиване и избраните продукти, върху които те ще се разпределят;  

- **Свързан документ** - полетата в тази колона се обзавеждат автоматично с тип, номер и дата на документ, в който участва продуктът на текущия ред;  

- **Метод за разпределение** - полето се обзавежда автоматично с метод **Отчетна стойност**;  
С него системата автоматично разпределя общата сума на разхода спрямо единичната цена на продуктите.  
Методът за разпределение може да бъде променен чрез падащия списък в полето.  

- **Сума за разпределяне** - данните в тези полета се обзавеждат автоматично спрямо избрания метод за разпределение;  

> Единствено при избран метод **Ръчно** в колона **Сума за разпределяне** се допуска редакция на стойностите.  

- **Сума на единица** - тези полета се попълват автоматично от системата със сумите на разпределените разходи за единица продукт;  

![](909-purchases-transport-expenses4.png){ class=align-center w=15cm }

С бутон **OK** се отваря форма за преминаване към следваща стъпка в разпределението на разходи.  

Вариантите за избор във формата са:  
     - **Да** - избраното разпределение се потвърждава и формата с редове от свързани документи се затваря автоматично;  
     С това цените на придобиване в складовите документи са актуализирани.    
     - **Не** - разпределението се отхвърля и формата с редове от свързани документи се затваря;  
     - **Отказ** - разпределението се прекъсва, като формата с редове от свързани документи остава на екран;   

![](909-purchases-transport-expenses5.png){ class=align-center w=15cm }

___   
## Свързани статии

- [Как да разпределим разходи по покупка](https://www.unicontsoft.com/cms/node/148)  
- [Разпределение на разходи за придобиване](https://docs.unicontsoft.com/blog/20240411-allocate-acquisition-costs.html)