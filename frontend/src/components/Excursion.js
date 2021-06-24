import React, { Component } from "react";
import { Container, Row, Jumbotron, Carousel} from 'react-bootstrap';
import '../static/css/excursion.css';
import '../static/css/buscar.css';
import { BiLike} from "react-icons/bi";

class Excursion extends Component {

	constructor(props) {
		super(props)

		this.state = {
			excursion: {}
		}
	}

	componentDidMount() {

		const { match: { params } } = this.props;

		const url = 'http://localhost:90/api/excursion/' + params.id + '/'

		// una promise, que devuelve otra promise
		fetch(url)
			.then(res => res.json())
			.then(res => {
						console.log(res)
						this.setState({excursion:res})   // Se cambia el state y re-renderiza
					})
			.catch(error => {
				alert('Error '+ error)
			})
	}

	render() {

		var tags = "";

		if(this.state.excursion.tags){

			this.state.excursion.tags.forEach(tag =>{
				tags += "#" + tag + " ";
			})
		}

		var listaImagenes= "";

		if(this.state.excursion.fotos){
			listaImagenes = this.state.excursion.fotos.map(foto =>{
				return(
					<Carousel.Item>
						<img src={require('../static/images/'+foto.foto).default} 
							alt={foto.pie} className="d-block w-100"/>
					</Carousel.Item>
				);
			});	
		}

		var listaComentarios = ""

		if(this.state.excursion.comentarios){
			listaComentarios = this.state.excursion.comentarios.map(comentario =>{
				return(<Container className="jumbotron comentario">
					<h6 className="font-weight-bold row">{comentario.autor}</h6>
					<p className="row">{comentario.contenido}</p>
				</Container>);
			})
		}		

		return (  
			<div>
				<Container>
					<Jumbotron className="titulo">
						<h2 className="font-weight-bold">{this.state.excursion.nombre}</h2>
					</Jumbotron>
				</Container>

				<Container className="foto">
					<Carousel className="carousel slide" data-bs-ride="carousel">
						{listaImagenes}
					</Carousel>
				</Container>

				<Container className="tags-likes">
					<Row>
						<div className="col-10 tags">
						<h5 className="mb-2 text-muted">{tags}</h5>
						</div>
						<Row className="col likes-container align-items-center">
							<button className="btn btn-primary like" type="submit">
								<BiLike/>
							</button>
							<Container className="col">
								<p class="likes">{this.state.excursion.likes}</p>
							</Container>
						</Row>
					</Row>
				</Container>

				<Container className="descripcion">
					<h5>{this.state.excursion.descripción}</h5>
				</Container>

				<Container className="comentarios">
					<h4 className="titulo font-weight-bold">Comentarios</h4>
					{listaComentarios}
				</Container>
			</div>
		);
	}
}

export default Excursion;