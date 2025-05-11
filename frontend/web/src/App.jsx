import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'


import LandingPage from './pages/LandingPage'
import Dashboard from './pages/Dashboard'
import AnalyzePage from './pages/AnalyzePage'
import PortfolioPage from './pages/PortfolioPage'
import ProfilePage from './pages/ProfilePage'
import AboutPage from './pages/AboutPage'

import './App.css'


function App() {

  return (
      <Routes>
        <Route path="/" element={<LandingPage/>}/>
        <Route path="/dashboard" element={<Dashboard/>}/>
        <Route path="/analyze" element={<AnalyzePage/>}/>
        <Route path="/portfolio" element={<PortfolioPage/>}/>
        <Route path="/profile" element={<ProfilePage/>}/>
        <Route path='/about' element={<AboutPage/>}/>
      </Routes>
  );
}

export default App
