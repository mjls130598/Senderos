import logo from './static/images/logo.gif';
import diputacion from './static/images/diputacion.png';
import './App.css';
import './static/css/base.css';
import { Navbar, Container, Nav, Jumbotron, Image } from 'react-bootstrap';
import React, { Component } from "react";
import { BrowserRouter, Route, Switch } from 'react-router-dom';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }
  render() {
    return (
      <div>
        <header>
          <Navbar className="navbar navbar-expand-lg navbar-dark bg-dark text-uppercase font-weight-bold">
            <Container fluid>
              <Navbar.Collapse className="d-flex justify-content-center">
                <Nav className="me-auto mb-2 mb-lg-0">
                  <Nav.Link className="active">Destinos</Nav.Link>
                  <Nav.Link className="active">Planea tu viaje</Nav.Link>
                  <Nav.Link className="active">Cosas que hacer</Nav.Link>
                  <Nav.Link href="/" className="active"><Image src={logo} thumbnail/></Nav.Link>
                  <Nav.Link className="active">Agenda cultural</Nav.Link>
                  <Nav.Link className="active">Área profesional</Nav.Link>
                  <Nav.Link className="active">Mi Granada</Nav.Link>
                </Nav>
              </Navbar.Collapse>
            </Container>
          </Navbar>
        </header>

        <body>
          <Jumbotron className="text-center">
            <h4 className="font-weight-bold">Turismo rural, activo y de naturaleza</h4>
          </Jumbotron>

          <BrowserRouter>
            <Switch>
              <Route path="/buscar">
                <Buscar />
              </Route>
              <Route path="/excursion">
                <Excursiones />
              </Route>
              <Route path="/excursion/:id">
                <Excursion />
              </Route>
            </Switch>
          </BrowserRouter>

        </body>

        <footer className="bg-dark text-white">
          <Container footer>
            <Image src={diputacion} alt="Diputación de Granada"/>
            <div className="float-right">
              <ul className="list-unstyled mb-0">
                <li>
                  <a href="https://www.turgranada.es/patronato-provincial-de-turismo/" className="text-white">Patronato Provincial de Turismo Diputación de Granada</a>
                </li>
                <li>
                  Cárcel Baja, 3. 18001. Granada
                </li>
                <li>
                  Tel: +34 958 24 71 46
                </li>
                <li>
                  Fax: +34 958 24 71 29
                </li>
              </ul>
            </div>
          </Container>
        </footer>
      </div>
    );
  }
}

export default App;
