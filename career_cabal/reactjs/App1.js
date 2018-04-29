import React from "react"
import { render } from "react-dom"
import Board from 'react-trello'
import axios from 'axios'

class App1 extends React.Component {

	state = {
		board : {
			lanes: [
				{
					id: 'lane1',
					title: 'Planned Tasks',
					label: '2/2',
					cards: [
						{id: 'Card1', title: 'Write Blog', description: 'Can AI make memes', label: '30 mins'},
						{id: 'Card2', title: 'Pay Rent', description: 'Transfer via NEFT', label: '5 mins', metadata: {sha: 'be312a1'}}
					]
				},
				{
					id: 'lane2',
					title: 'Completed',
					label: '0/0',
					cards: []
				}
			]
		}

	};

	constructBoard(lanes,applications) {
		var all_applications = applications["applications"];
		var lane_cards = {};
		for (var x=0;x<all_applications.length;x++) {
			var application = all_applications[x];
			var card_lane = application["status"];
			var card = {id : application["id"], title : application["job"]["title"], description : application["job"]["company"]["name"]};
			if (lane_cards[card_lane] == undefined) {
				lane_cards[card_lane] = [card];
			}
			else {
				lane_cards[card_lane] = lane_cards[card_lane].concat(card);

			}


		}

		var main = lanes["main"];
		var lanes_array = [];
		for(var x=0;x<main.length;x++) {
			var lane_id = main[x]["id"];
			var lane_description = main[x]["description"];
			if (lane_cards[x] == undefined) {
				lane_cards[x] = [];
			}
			lanes_array = lanes_array.concat( {id : lane_id, title : lane_description,cards : lane_cards[x]});
		}

		var board = {lanes : lanes_array};
		return board;
	}
	componentDidMount() {
		axios.all([
			axios.get('/application/lanes'),
			axios.get('/application/applications')
		])
			.then(axios.spread((lanes,applications) => {
				const newBoard = this.constructBoard(lanes.data,applications.data);
				const newState  = Object.assign({}, this.state, {board : newBoard})
				this.setState(newState);
			}))
			.catch(error => console.log(error));
	}
	render() {
		return  <Board data={this.state.board} draggable="true" />
	}
}

render(<App1/>, document.getElementById('App1'))
