"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Shield, Mail, Phone, Lock, Cpu, LayoutDashboard, Database, Activity, Settings, Power } from "lucide-react";

export default function Home() {
  const [authenticated, setAuthenticated] = useState(false);
  const [authStep, setAuthStep] = useState(1);
  const [activeTab, setActiveTab] = useState("mission");
  const [isAutoPilot, setIsAutoPilot] = useState(false);

  // Authentication Flow
  const handleAuth = () => {
    if (authStep < 5) {
      setAuthStep(authStep + 1);
    } else {
      setAuthenticated(true);
    }
  };

  if (!authenticated) {
    return (
      <div className="min-h-screen flex items-center justify-center p-4 bg-black overflow-hidden bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-omega-950/20 via-black to-black">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="w-full max-w-md p-8 glass rounded-3xl space-y-8 relative z-10"
        >
          <div className="flex flex-col items-center space-y-4">
            <div className="p-4 bg-omega-500/10 rounded-2xl">
              <Shield className="w-12 h-12 text-omega-400 animate-pulse" />
            </div>
            <h1 className="text-3xl font-bold tracking-tighter">OMEGA VAULT</h1>
            <p className="text-omega-400/60 text-sm font-medium">Step {authStep} of 5: PILOT VERIFICATION</p>
          </div>

          <AnimatePresence mode="wait">
            <motion.div
              key={authStep}
              initial={{ opacity: 0, x: 10 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -10 }}
              className="space-y-6"
            >
              {authStep <= 3 && (
                <div className="space-y-4">
                  <div className="flex items-center space-x-2 text-omega-300">
                    <Mail className="w-4 h-4" />
                    <span className="text-sm">Sequence Email {authStep}</span>
                  </div>
                  <input
                    type="password"
                    placeholder="Enter Sequence Token..."
                    className="w-full bg-white/5 border border-white/10 rounded-xl p-4 outline-none focus:border-omega-500 transition-colors"
                  />
                </div>
              )}
              {authStep === 4 && (
                <div className="space-y-4">
                  <div className="flex items-center space-x-2 text-omega-300">
                    <Phone className="w-4 h-4" />
                    <span className="text-sm">Hardware Link (SMS)</span>
                  </div>
                  <input
                    type="password"
                    placeholder="Enter Hardware Token..."
                    className="w-full bg-white/5 border border-white/10 rounded-xl p-4 outline-none focus:border-omega-500 transition-colors"
                  />
                </div>
              )}
              {authStep === 5 && (
                <div className="space-y-4">
                  <div className="flex items-center space-x-2 text-omega-300">
                    <Cpu className="w-4 h-4" />
                    <span className="text-sm">Neural Security Question</span>
                  </div>
                  <p className="text-xs text-white/40">What was the first AGI protocol name?</p>
                  <input
                    type="text"
                    placeholder="Answer..."
                    className="w-full bg-white/5 border border-white/10 rounded-xl p-4 outline-none focus:border-omega-500 transition-colors"
                  />
                </div>
              )}

              <button
                onClick={handleAuth}
                className="w-full py-4 rounded-xl omega-gradient font-bold hover:opacity-90 transition-opacity"
              >
                VALIDATE IDENTITY
              </button>
            </motion.div>
          </AnimatePresence>
        </motion.div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-black flex text-white/90">
      {/* Sidebar */}
      <div className="w-72 glass border-r border-white/5 p-6 flex flex-col space-y-8">
        <div className="flex items-center space-x-3 px-2">
          <div className="w-8 h-8 rounded-lg omega-gradient flex items-center justify-center">
            <Shield className="w-5 h-5 text-white" />
          </div>
          <span className="font-bold text-xl tracking-tighter">JARVIS v2</span>
        </div>

        <nav className="flex-1 space-y-2">
          {[
            { id: "mission", name: "Mission Board", icon: LayoutDashboard },
            { id: "memory", name: "Memory Lab", icon: Database },
            { id: "hive", name: "Hive Swarm", icon: Activity },
            { id: "settings", name: "Setup Vault", icon: Settings },
          ].map((item) => (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center space-x-3 px-4 py-3 rounded-xl transition-all ${activeTab === item.id ? "bg-white/10 text-omega-400 font-bold" : "hover:bg-white/5 text-white/50"
                }`}
            >
              <item.icon className="w-5 h-5" />
              <span>{item.name}</span>
            </button>
          ))}
        </nav>

        <div className="p-4 glass rounded-2xl space-y-4">
          <div className="flex items-center justify-between">
            <span className="text-xs font-medium text-white/40">AUTO-PILOT</span>
            <button
              onClick={() => setIsAutoPilot(!isAutoPilot)}
              className={`w-10 h-5 rounded-full transition-colors relative ${isAutoPilot ? "bg-omega-500" : "bg-white/10"}`}
            >
              <div className={`absolute top-1 w-3 h-3 rounded-full bg-white transition-all ${isAutoPilot ? "right-1" : "left-1"}`} />
            </button>
          </div>
          <div className="flex items-center space-x-2 text-[10px] text-omega-400/60 font-mono">
            <div className="w-1.5 h-1.5 rounded-full bg-omega-400 animate-pulse" />
            <span>SYSTEM ONLINE</span>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <main className="flex-1 p-8 space-y-8 overflow-y-auto">
        <header className="flex justify-between items-center">
          <div>
            <h2 className="text-3xl font-bold tracking-tight">
              {activeTab === "mission" && "Active Operations"}
              {activeTab === "memory" && "Pattern Repository"}
              {activeTab === "hive" && "Agent Swarm"}
              {activeTab === "settings" && "Configuration Vault"}
            </h2>
            <p className="text-white/40 text-sm mt-1">Omega Ecosystem Local Ground Truth</p>
          </div>
          <div className="flex space-x-4">
            <button className="px-6 py-2.5 glass rounded-xl text-sm font-semibold hover:bg-white/5 transition-colors">
              GENERATE BACKUP
            </button>
            <button className="px-6 py-2.5 omega-gradient rounded-xl text-sm font-bold hover:opacity-90 transition-opacity">
              SYNC TO GITHUB
            </button>
          </div>
        </header>

        {/* Dynamic Tab Content */}
        {activeTab === "mission" && (
          <div className="grid grid-cols-4 gap-6">
            {["PENDING", "BUILDING", "BLOCKED", "STABLE"].map((status) => (
              <div key={status} className="space-y-4">
                <div className="flex items-center justify-between px-1">
                  <span className="text-[10px] font-bold tracking-widest text-white/30">{status}</span>
                  <span className="text-[10px] font-mono text-omega-500">2</span>
                </div>
                <div className="min-h-[200px] glass rounded-2xl p-4 space-y-4">
                  <div className="p-4 bg-white/5 rounded-xl border border-white/5 hover:border-omega-500/30 transition-colors cursor-pointer group">
                    <h4 className="text-sm font-bold group-hover:text-omega-400">Initialize Next.js Hybrid</h4>
                    <p className="text-[10px] text-white/40 mt-2">Task ID: OMEGA-042</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {activeTab === "memory" && (
          <div className="glass rounded-3xl p-8 min-h-[400px] flex items-center justify-center text-white/20 italic font-light">
            Accessing Hippocampus... Memory retrieval in progress.
          </div>
        )}
      </main>
    </div>
  );
}
