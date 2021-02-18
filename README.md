## Run and stop app
`make run`

`make stop`

## Open app
[0.0.0.0:8002/api/](https://0.0.0.0:8002/api/)

## Login as admin
Select "Log in" and type:

Username: admin

Password: admin

## Creating menu
If you want to add something to the menu, you should login as admin.
If you are logged in, go to the [0.0.0.0:8002/api/](https://0.0.0.0:8002/api/)
and select what would you like to add (Card or Dish). Now just fill up the form and select "POST".

## Filtering cards
You can filter results by adding `GET` parameters to the url.
Filtering works only for cards: [0.0.0.0:8002/api/cards/?name=asc](https://0.0.0.0:8002/api/cards/?name=asc)

#### Allowed filters:
`name` - filtering by name
`dish` - filtering by number of dishes in card
`created_on` - filtering by created date
`updated_on` - filtering by updated date

You can filter ascending and descending, and you can combine parameters, for example:
[0.0.0.0:8002/api/cards/?name=asc&dish=desc](https://0.0.0.0:8002/api/cards/?name=asc&dish=desc)
