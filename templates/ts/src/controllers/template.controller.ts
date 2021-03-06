async function getREPLACEMEs(): any[] {
  return new Promise<any>();
}
async function getREPLACEME(id: string): any {
  return new Promise<any>();
}
async function deleteREPLACEME(id: string): boolean {
  return new Promise<boolean>();
}
async function updateREPLACEME(obj: any): boolean {
  return new Promise<boolean>();
}
async function createREPLACEME(obj: any): string {
  return new Promise<boolean>();
}

export {
  getREPLACEME,
  getREPLACEMEs,
  deleteREPLACEME,
  updateREPLACEME,
  createREPLACEME,
};
