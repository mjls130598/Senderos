import React, { Component } from "react";
import { Form, Container, Button, Row } from 'react-bootstrap';
import '../static/css/buscar.css';
import '../static/css/cards.css';
import { BiSearch } from "react-icons/bi";
import Cards from './Excursion-cards';


class Buscar extends Component {

	constructor(props) {
		super(props);

		this.state = {
			excursiones: []
		};
	}

	componentDidMount() {
		const url = 'http://localhost:8000/api/excursiones/'

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
			<div>
				<Container className="titulo">
					<h2 className="font-weight-bold">Excursiones y turismo</h2>
				</Container>
				<Container className="jumbotron buscador">
					<Form className="buscador-formulario">
						<div className="input-group mb-3">
							<Form.Control type="text" placeholder="Término de búsqueda" aria-label="Término de búsqueda" aria-describedby="buscador"/>
							<select className="btn-secondary">
								<option>Municipio</option>
								<option>Alcudia</option>
								<option>Esfiliana</option>
								<option>Guadix</option>
								<option>Granada</option>
								<option>Órgiva</option>
								<option>Puente Genil</option>
								<option>Turón</option>
								<option>Otro</option>
							</select>
							<Button type="button" className="btn btn-primary pull-right">
							Buscar <BiSearch/>
							</Button>
						</div>
					</Form>
				</Container>

				<Container className="excursiones">
					<Row className="row-cols-3">
					{
						listaExcursiones
					}
					</Row>
				</Container>
			</div>
		);
	}
}
export default Buscar;