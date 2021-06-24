import React, { Component } from "react";
import { Container, Row } from 'react-bootstrap';
import '../static/css/cards.css'
import Cards from './Excursion-cards';


class Excursiones extends Component {

	constructor(props) {
		super(props);

		this.state = {
			excursiones: []
		};
	}

	componentDidMount() {
		const url = 'http://localhost:90/api/excursiones/'

		// una promise, que devuelve otra promise
		fetch(url)
			.then(res => res.json())
			.then(res => {
						console.log(res)
						this.setState({excursiones:res})   // Se cambia el state y re-renderiza
					})
			.catch(error => {
				alert('Error '+ error)
			})
	}

	render() {

		const listaExcursiones = this.state.excursiones.map(ex =>{
			return (<Cards excursion = {ex}/>);
		})

		return (  
			<Container className="excursiones">
					<Row className="row-cols-3">
					{
						listaExcursiones
					}
					</Row>
				</Container>
		);
	}
}
export default Excursiones;