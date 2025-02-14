import {Component} from '@angular/core';
import {EmpleadoComponent} from '../empleado/empleado.component';

@Component({
  selector: "app-empleados",
  templateUrl: "./empleados.component.html",
  imports: [
    EmpleadoComponent
  ],
  styleUrl: './empleados.component.css'
})
export class EmpleadosComponent{

}
