# ***Euclidean-Algorithm***
> ## - *Библиотека, а точнее пакет, для вычисления НОД двух чисел*
#
## ***Установка***
### ***для начала зайдите в терминал и подготовьте к работе виртуальное окружение***
> #### *Сначала его нужно создать:* `python -m venv venv`
######
> #### *После чего активировать:*
> `venv\Scripts\activate.bat` - *для Windows*
> ######
> `source venv/bin/activate` - *для Linux и macOS*
>> #### *Теперь,* 
>>> ***даже если у вас уже было активировано виртуальное окружение,*** 
>> #### *мы можем переходить к установке самого пакета*
> #### ***P.S: Если у вас не получилось активировать виртуальное окружение, то добавьте его в настройках интерпретатора или создайте новый проект с ним***
####
### ***Для установки пакета нужно прописать следующую команду в терминале:***
### `pip install euclidean-algorithm`
#
## ***Эксплуатация***
### ***Давайте узнаем НОД чисел 3444 и 983752:***
[![2024-12-08_16-22-18.png](https://s.iimg.su/s/08/6Wqgzksf4qGzC9meWuzXbSZNISMgi5EqT5RTt2Sv.png)](https://iimg.su/i/ao90H)
> ***Импортируем основную функцию и передаём числа***
>    ```python
>    from euclidean_algorithm.euclidean_algorithm import euclidean_algorithm
>    
>    
>    print(euclidean_algorithm(3444, 983752))
>    ```
>    ### ***НОД равен 28***
#
## ***Исключения***
#
[![2024-12-08_16-25-06.png](https://s.iimg.su/s/08/hkEqCaBzSmVOaMh2qHgsej7oZcBO0htKTRI196ix.png)](https://iimg.su/i/N1Za7)
>> ### euclidean_algorithm.euclidean_algorithm.EuclideanAlgorithmValueError
> ### ***если число меньше 1***
#
[![2024-12-08_16-28-05.png](https://s.iimg.su/s/08/CJowretz0kNUSFwXlsOPr7dotVbzCKvLta8j6ruu.png)](https://iimg.su/i/2NMin)
>> ### euclidean_algorithm.euclidean_algorithm.EuclideanAlgorithmLengthError
> ### ***если количество цифр в числе больше 20***
