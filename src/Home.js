import React from 'react'
import PermutationInputs from './PermutationInputs/PermutationInputs'
import Calculator from './PermutationInputs/Calculator'
import {Routes, Route} from 'react-router-dom'
import './Home.css'

function Home() {
  return (
    <div className='home'>
        <Routes>
        <Route path="/" element={<PermutationInputs />}/>
        <Route path='/calculator' element={<Calculator />} />
        </Routes>
    </div>
  )
}

export default Home
