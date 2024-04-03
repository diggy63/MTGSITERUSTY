export function findCards(searchQ) {
    return fetch(`api/cards/exact/${searchQ}`, {
      method: "get",
    }).then((resp) => {
      if (resp.ok) return resp.json();
      throw new Error("could not find");
    });
  }
  
