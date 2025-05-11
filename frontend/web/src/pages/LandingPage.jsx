import React from 'react'

const LandingPage = () => {
  return (
      <div
        className='w-full min-h-screen bg-[#0F172A] text-white px-10 py-20'
      >
        <h1
            className='text-6xl font-extrabold mb-6'
        >
            Welcome to Stock Analyzer
        </h1>

        <p
          className='text-xl max-w-3xl leading-relaxed'
        >
          Empowering traders with machine-learning driven insights and advanced technical analysis.
          Built to help you buy smarter, sell faster, and never miss the opportunity.
        </p>
        <button
          className='mt-10 px-6 py-3 bg-gradient-to-r from-blue-500 to-cyan-400 text-white rounded-lg text-lg font-semibold hover:scale-105 transition'
        >
          Try it Now
        </button>

      </div>
  )
}

export default LandingPage

