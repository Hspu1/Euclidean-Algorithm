# ***Euclidean-Algorithm***
> ## - *Библиотека, а точнее пакет, для вычисления НОД двух чисел*
###
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
###
## ***Эксплуатация***
### ***Давайте узнаем НОД чисел 3444 и 983752:***
> ***Импортируем основную функцию и передаём числа***
>    ```python
>    from euclidean_algorithm.euclidean_algorithm import euclidean_algorithm
>    
>    
>    print(euclidean_algorithm(3444, 983752))
>    ```
>    ### ***НОД равен 28***
[![2024-12-08_16-22-18.png](https://s.iimg.su/s/08/th_kW5VQvuBA4DQDAm0VpJI6FKvGUVwBK84rEML2WSw.png)](https://iimg.su/i/IMjv7)
### ***Исключения***
> #### Если вы передадите число меньше 1 или число, количество цифр в котором превышает 20,
> #### то вы на выходе получите ошибку:
###
>> euclidean_algorithm.euclidean_algorithm.EuclideanAlgorithmValueError
> ##### ***если число меньше 1***
[![2024-12-08_16-25-06.png](https://s.iimg.su/s/08/th_hkEqCaBzSmVOaMh2qHgsej7oZcBO0htKTRI196ix.png)](https://iimg.su/i/N1Za7)
###
>> euclidean_algorithm.euclidean_algorithm.EuclideanAlgorithmLengthError
> ##### ***если кол-во цифр в числе больше 20***
[![2024-12-08_16-28-05.png](https://s.iimg.su/s/08/th_0vJZlNG6TZZnJq1YtjUiujPqR5Fw9GI1WBeLI912.png)](https://iimg.su/i/XDFlG)
