import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {Title} from '@angular/platform-browser';
import {EmpleadosComponent} from './empleados/empleados.componente';
import {EmpleadoComponent} from './empleado/empleado.component';

@Component({
  selector: 'app-raiz',
  imports: [RouterOutlet, EmpleadosComponent, EmpleadoComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'MiProyecto';

  saludo = "Hola como estamos"
  protected readonly Title = Title;
}
