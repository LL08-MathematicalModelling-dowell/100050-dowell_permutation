import React from 'react'
import { useDispatch } from 'react-redux'
import { useSelector } from 'react-redux'
import { assignIsClicked } from '../app/features/counter/CounterSlice'
import axios from 'axios'
import SData from './SData'
import './SetrBox.css'

function SetrBox({rData}) {

  const dispatch = useDispatch()

  const insertedId = useSelector((state) => state.userId.inserted_id)
  const email = useSelector((state) => state.userId.email)
  const r = useSelector((state) => state.userId.r)
  const rCount = useSelector((state) => state.userId.rcount)
  const strArray = rData.split(",")
  let rArray = []

  const addArray = () =>{
    for(let i = 0; i<strArray.length; i++){
      rArray.push(`"${strArray[i]}"`)
    }
  }

  addArray()
  console.log("This is rcount",rCount)
  console.log("This is r",r)
  const savePermutation = async () =>{
    dispatch(assignIsClicked(false))
    if(rCount === Number(r)) {
    try{
      const resp = await axios.post(
        'https://100050.pythonanywhere.com/permutationapi/api/', {
          "inserted_id":insertedId,
          "selectedPermutation":rArray,
          "email": email,
          "command":"savePermutation"
  })
  console.log(resp.data.message)
  let pvar = resp.data.message
  console.log(pvar.substring(pvar.indexOf("["), pvar.indexOf("]")+1))
  }catch(err){
    console.log(err.response)
  }
  } else {
    try{
      const resp = await axios.post(
        'https://100050.pythonanywhere.com/permutationapi/api/', {
          "inserted_id":insertedId,
          "selectedPermutation":rArray,
          "command":"savePermutation"
  })
  console.log(resp.data.message)
  let pvar = resp.data.message
  console.log(pvar.substring(pvar.indexOf("["), pvar.indexOf("]")+1))
  }catch(err){
    console.log(err.response)
  }
  }
  }

  const clicked = () =>{
    savePermutation()
    SData.push(rData)
    dispatch(assignIsClicked(false))
  }
  return (
    <div className='setrBox' onClick={clicked}>
      {
        rData
      }
    </div>
  )
}

export default SetrBox
