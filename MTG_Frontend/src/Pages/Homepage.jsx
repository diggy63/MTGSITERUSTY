import React, { useState } from "react";
import TextField from '@mui/material/TextField'
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

import * as CardsApiServer from '../API/CardsApiServer'

export default function Homepage() {
  const [searchQ, setSearchQ ] = useState("")
  const [card_list, set_card_list] = useState([])

  async function HandleClick(){
    const cardInfo = await CardsApiServer.findCards(searchQ)
    console.log(cardInfo)
    set_card_list(cardInfo)
  }

  const view_cards_list = card_list.map((card_list,index) =>{
    return (
      <Card sx={{ minWidth: 275 }}>
        <CardContent>
          <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
            {card_list.type}
          </Typography>
          <Typography variant="h5" component="div">
            {card_list.name}
          </Typography>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            {card_list.card_text}
          </Typography>
          {card_list.set_code}
          {card_list.power}/{card_list.toughness}
        </CardContent>
      </Card>
    );
  })

  return (
    <>
      <h1>Homepage</h1>
      <TextField id="outlined-basic" label="Outlined" value={searchQ} variant="outlined" onChange={e => setSearchQ(e.target.value)} />
      <Button variant="outlined" onClick={HandleClick}>Outlined</Button>
      {view_cards_list}
    </>
  );
}
