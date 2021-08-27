# Receptek-web

Weboldal a receptek adatbázis eléréséhez, frissítéséhez.
Ha minden igaz, akkor ide nem kell jönnie, csak azoknak akik fejlesztik, ez a leírás csak nekik szól.


## Telepítés:

### Letöltés
```shell
> git pull https://github.com/Mooky0/receptek-web.git
> cd receptek-web
```

### venv létrehozás

Ez nem kötelező, de a tisztaság érdekében ajánlott.

```shell
> python3 -m venv venv
```

Ha `cmd` -t használsz:
```shell
> ./venv/Scripts/activate.bat
```

Ha `PS` -t használsz:
```shell
> ./venv/Scripts/Activate.ps1
```

A virtuális környezetet kikapcsolni mindkét esetben a `deactivate` paraccsal tudod.

## Használat

Aktiváld ha `venv` -et ha még nem tetted.

A kiekészítések telepítése
```shell
> pip install -r requirements.txt
```

### Futtatás venv-el
```shell
> ./venv/Scripts/python.exe ./app.py
```

### Futtatás venv nélkül
```shell
> python ./app.py
```
vagy az `app.py` file futtatása.

És a `localhost:5000/index` -en fog futni az oldal, bármely böngészőből elérhető az oldal.
Teszt fázisban csakk a gépen amin fut.

Leállítani a <kbd>Ctrl</kbd> + <kbd>C</kbd> billentyűkombinációval tudod.

------

Contact: tothgabor2003@gmail.com
