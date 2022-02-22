"use strict"

const express = require('express');
const catalyst = require('zcatalyst-sdk-node');

const app = express();
app.use(express.json());

app.post("/stream", (req, res) => {
	console.log("\nBody: " + JSON.stringify(req.body));
	// res.status(200).json(eq.body);
	let catalystApp = catalyst.initialize(req, { type: catalyst.type.applogic });

	//Get table meta object without details.
	let table = catalystApp.datastore().table('flespistream');

	//Use Table Meta Object to insert the row which returns a promise
	let insertPromise = table.insertRow({
		data: JSON.stringify(req.body)
	});

	insertPromise
		.then((row) => {
			console.log("\nInserted Row : " + JSON.stringify(row));
			res.status(200).json(row);
		})
		.catch((err) => {
			console.log(err);
			res.status(500).send(err);
		});
});

app.all("/", (req, res) => {

	res.status(200).send("I am Live and Ready.");

});

module.exports = app;
