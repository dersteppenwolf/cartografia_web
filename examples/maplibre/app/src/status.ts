export function setStatus(message: string, isError = false): void {
  const status = document.querySelector<HTMLParagraphElement>("#estado");
  if (!status) return;
  status.textContent = message;
  status.dataset.state = isError ? "error" : "ready";
}
