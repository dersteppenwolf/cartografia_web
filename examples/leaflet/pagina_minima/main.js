import { setStatus } from './status.js';

const button = document.querySelector('#actualizar-estado');
const status = document.querySelector('#estado');

button.addEventListener('click', () => {
  setStatus(status, 'El módulo ES actualizó este mensaje.');
});
