import React, { Component } from "react";
import { Card } from 'react-bootstrap';

class Cards extends Component {

	constructor(props) {
		super(props)
	}

	render() {

		var tags = ""
		
		this.props.excursion.tags.forEach(tag =>{
			tags += "#" + tag + " ";
		})

		return (  
			<Card className="col" id="excursion">
				<Card.Img variant="top" src={require('../static/images/'+this.props.excursion.fotos[0].foto).default} 
					alt={this.props.excursion.fotos[0].pie}/>
				<Card.Body>
					<Card.Title>{this.props.excursion.nombre}</Card.Title>
					<Card.Subtitle className="mb-2 text-muted">{tags}</Card.Subtitle>
					<Card.Text>{this.props.excursion.descripción}</Card.Text>
					<a href={"/excursion/" + this.props.excursion.id} 
						className="btn btn-primary enlace-excursion">Más detalle</a>
				</Card.Body>
			</Card>
		);
	}
}
export default Cards;