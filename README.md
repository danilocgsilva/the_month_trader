# The month trader

Personal stock market watcher and manager for personal usage.

## To start

In the root folder, type:
```
flask run
```

## Sidenotes for migrations

Everytime a chnage in the database structure through `models.py`, you must generate, and run, a migration.

If the no migration has not runned in the environment, you must first *initiate* the database migration with:

```
flask db init
```

The steps to proceed for database changes, follows those two commands:

```
flask db migrate -m "<A migration name defining changes>"
flask db upgrade
```
