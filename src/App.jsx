import React, { useState, useRef } from "react";

export default function SmartMirrorApp() {
  const [page, setPage] = useState("home");
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const fileRef = useRef(null);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setPreview(URL.createObjectURL(file));
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      console.log("Backend Response:", data);

      setResult(data);
      setPage("result");
    } catch (err) {
      console.error("Upload Error:", err);
      alert("Backend connection failed");
    }

    setLoading(false);
  };

  const card =
    "bg-white/80 backdrop-blur-lg rounded-3xl shadow-xl border border-gray-200 p-6 hover:shadow-2xl transition duration-300";

  const btn =
    "bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-4 rounded-2xl font-bold hover:scale-105 transition duration-300 shadow-lg";

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-100 via-blue-50 to-indigo-100 p-6">
      
      {/* HOME PAGE */}
      {page === "home" && (
        <div className="max-w-6xl mx-auto text-center py-16">
          <h1 className="text-7xl font-bold text-gray-900">Smart Mirror</h1>

          <p className="text-2xl text-blue-600 font-semibold mt-4">
            AI Personal Assistant
          </p>

          <p className="text-xl text-gray-600 mt-6 max-w-3xl mx-auto leading-9">
            Smart assistant for blind and visually impaired users.
          </p>

          <button
            className={`${btn} mt-16 text-xl`}
            onClick={() => setPage("input")}
          >
            Start Smart Mirror →
          </button>
        </div>
      )}

      {/* INPUT PAGE */}
      {page === "input" && (
        <div className="max-w-5xl mx-auto py-16 text-center">
          <button
            className="mb-10 text-lg font-semibold"
            onClick={() => setPage("home")}
          >
            ← Back
          </button>

          <h1 className="text-6xl font-bold">Choose Your Input</h1>

          <div className="mt-16">
            <div className={card}>
              <h2 className="text-3xl font-bold">🖼 Upload Image</h2>

              <input
                ref={fileRef}
                type="file"
                accept="image/*"
                onChange={handleUpload}
                className="mt-8 block mx-auto"
              />
            </div>
          </div>

          {loading && (
            <p className="mt-10 text-xl font-semibold">
              Analyzing image...
            </p>
          )}
        </div>
      )}

      {/* RESULT PAGE */}
      {page === "result" && result && (
        <div className="max-w-6xl mx-auto py-10">
          <button
            className="mb-10 text-lg font-semibold"
            onClick={() => setPage("input")}
          >
            ← Back
          </button>

          <h1 className="text-5xl font-bold text-center">
            Your Analysis Results
          </h1>

          {preview && (
            <img
              src={preview}
              alt="preview"
              className="mx-auto mt-10 rounded-3xl w-96 shadow-2xl"
            />
          )}

          <div className="grid md:grid-cols-2 gap-8 mt-12">
            
            {/* CLOTHING */}
            <div className={card}>
              <h2 className="text-3xl font-bold">👕 Clothing</h2>
              <p className="mt-4 text-lg">
                Type: {result.clothing?.type || "Not detected"}
              </p>
              <p className="text-lg">
                Confidence:{" "}
                {result.clothing?.confidence
                  ? (result.clothing.confidence * 100).toFixed(1)
                  : "0"}
                %
              </p>
            </div>

            {/* HAIRSTYLE */}
            <div className={card}>
              <h2 className="text-3xl font-bold">💇 Hairstyle</h2>
              <p className="mt-4 text-lg">
                Status: {result.hairstyle?.status || "Unknown"}
              </p>
              <p className="text-lg">
                Hair Type: {result.hairstyle?.hair_type || "Unknown"}
              </p>
              <p className="mt-2 text-lg">
                Suggestion:{" "}
                {result.hairstyle?.suggestion || "No suggestion"}
              </p>
            </div>

            {/* POSTURE */}
            <div className={card}>
              <h2 className="text-3xl font-bold">🧍 Posture</h2>
              <p className="mt-4 text-lg">
                {result.posture?.posture || "Not detected"}
              </p>
              <p className="text-lg">
                {result.posture?.suggestion || ""}
              </p>
            </div>

            {/* SUGGESTIONS */}
            <div className={card}>
              <h2 className="text-3xl font-bold">💡 Suggestions</h2>
              <ul className="mt-4 list-disc pl-5">
                {result.suggestions?.length > 0 ? (
                  result.suggestions.map((s, i) => (
                    <li key={i} className="mb-2 text-lg">
                      {s}
                    </li>
                  ))
                ) : (
                  <li>No suggestions available</li>
                )}
              </ul>
            </div>
          </div>

          <div className="text-center mt-12">
            <button className={btn} onClick={() => setPage("input")}>
              Analyze Another Photo
            </button>
          </div>
        </div>
      )}
    </div>
  );
}