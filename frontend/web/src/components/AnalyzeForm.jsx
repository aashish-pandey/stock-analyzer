import { useState } from "react";

export default function AnalyzeForm({ onAnalyze }){
    const [ticker, setTicker] = useState('AAPL');

    const handleSubmit = (e) =>{
        e.preventDefault();
        onAnalyze(ticker.toUpperCase());
    };

    return (
        <form
            onSubmit={handleSubmit}
            className="flex flex-col sm:flex-row gap-4 items-center justify-center mt-10"
        >
            <input
                type="text"
                value={ticker}
                onChange={(e)=> setTicker(e.target.value)}
                className="border border-gray-300 rounded px-4 py-2 w-64 text-black"
                placeholder="Enter Stock ticker (e.g. AAPL)"
            />
            <button
                type="submit"
                className="bg-indigo-600 text-white px-6 py-2 rounded hover:bg-indigo-700 transition"
            >
                Analyze

            </button>

        </form>
    )
};