function getFullResponseFromAPI() {
  return new Promise((resolve, reject) => {
    if (succes) resolve({ status: 200, body: 'Succes'});
    reject(Error('The fake API is not working currently'));
  });
}

export default getFullResponseFromAPI;
