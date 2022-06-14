db.people.insertOne({
  sex: "male",
  first_name: "Rafal",
  last_name: "Szloda",
  job: "Junior Data Engineer",
  email: "s242145@pjwstk.edu.pl",
  location: {
    city: "Warszawa",
    address: { streetname: "Niemcewicza", streetnumber: "10102" },
  },
  description: "nice guy",
  height: "188",
  weight: "90",
  birth_date: "1996-11-20T01:01:01Z",
  nationality: "Poland",
  credit: {
    type: "switch",
    number: "5896543223752567890",
    currency: "PLN",
    balance: "00.00",
  },
})