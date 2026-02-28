"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Shield, Mail, Phone, Lock, Cpu, LayoutDashboard,
  Database, Activity, Settings, ChevronRight,
  Download, Github, Terminal, ExternalLink, Menu, X
} from "lucide-react";

export default function Home() {
  const [view, setView] = useState("landing"); // landing, auth, dashboard
  const [authStep, setAuthStep] = useState(1);
  const [activeTab, setActiveTab] = useState("mission");
  const [isAutoPilot, setIsAutoPilot] = useState(false);
  const [showDownloads, setShowDownloads] = useState(false);

  // --- HANDLERS ---
  const handleLoginStart = () => setView("auth");
  const handleAuth = () => {
    if (authStep < 5) {
      setAuthStep(authStep + 1);
    } else {
      setView("dashboard");
    }
  };

  const copyInstallCmd = () => {
    navigator.clipboard.writeText("git clone https://github.com/edsworld27/Omega-System.git");
    alert("Installation command copied to clipboard!");
  };

  // --- COMPONENTS ---

  const LandingPage = () => (
    <div className="min-h-screen bg-[#050505] text-white selection:bg-omega-500/30 overflow-hidden relative">
      {/* Background Decorative Elements */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
        <div className="absolute top-[-10%] right-[-10%] w-[40%] h-[40%] bg-omega-500/5 blur-[120px] rounded-full" />
        <div className="absolute bottom-[-10%] left-[-10%] w-[30%] h-[30%] bg-omega-900/10 blur-[100px] rounded-full" />
      </div>

      {/* Nav */}
      <nav className="flex items-center justify-between p-8 max-w-7xl mx-auto relative z-10">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl omega-gradient flex items-center justify-center shadow-[0_0_20px_rgba(14,165,233,0.3)]">
            <Shield className="w-6 h-6 text-white" />
          </div>
          <span className="font-bold text-2xl tracking-tighter">OMEGA</span>
        </div>
        <div className="flex items-center space-x-8">
          <button
            onClick={() => setShowDownloads(!showDownloads)}
            className="text-sm font-medium text-white/60 hover:text-white transition-colors relative"
          >
            Downloads
            {showDownloads && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="absolute top-full right-0 mt-4 w-64 glass rounded-2xl p-2 shadow-2xl z-20"
              >
                <a href="https://github.com/edsworld27/Omega-System" className="flex items-center space-x-3 p-3 hover:bg-white/5 rounded-xl transition-all">
                  <Database className="w-4 h-4 text-omega-400" />
                  <span className="text-xs">Omega System Repo</span>
                </a>
                <a href="https://github.com/edsworld27/omega-claw" className="flex items-center space-x-3 p-3 hover:bg-white/5 rounded-xl transition-all">
                  <Cpu className="w-4 h-4 text-omega-400" />
                  <span className="text-xs">Omega Claw Engine</span>
                </a>
                <button onClick={copyInstallCmd} className="w-full flex items-center space-x-3 p-3 hover:bg-white/5 rounded-xl transition-all text-left">
                  <Terminal className="w-4 h-4 text-omega-400" />
                  <span className="text-xs">Copy Install Command</span>
                </button>
              </motion.div>
            )}
          </button>
          <button
            onClick={handleLoginStart}
            className="px-6 py-2.5 glass rounded-full text-sm font-bold hover:bg-white/10 transition-all border border-white/10"
          >
            LOGIN
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <main className="max-w-7xl mx-auto px-8 pt-24 pb-32 relative z-10 flex flex-col items-center text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="space-y-8"
        >
          <div className="inline-flex items-center space-x-2 px-3 py-1 bg-omega-500/10 border border-omega-500/20 rounded-full text-[10px] font-bold tracking-[0.2em] text-omega-400">
            <Activity className="w-3 h-3" />
            <span>LOCAL AGI NEXUS v2.1</span>
          </div>

          <h1 className="text-7xl md:text-8xl font-black tracking-tighter leading-none bg-clip-text text-transparent bg-gradient-to-b from-white to-white/40">
            THE OMEGA <br /> <span className="text-omega-500">NEXUS</span>
          </h1>

          <p className="max-w-2xl mx-auto text-xl text-white/50 font-medium leading-relaxed">
            The multi-layered evolution of local intelligence. <br />
            Hardened security. Persistent autonomy. Absolute control.
          </p>

          <div className="flex items-center justify-center space-x-6 pt-8">
            <button
              onClick={handleLoginStart}
              className="px-10 py-5 omega-gradient rounded-2xl font-black text-lg shadow-[0_20px_40px_-10px_rgba(14,165,233,0.4)] hover:scale-105 transition-transform active:scale-95 flex items-center space-x-3"
            >
              <span>IGNITE MISSION CONTROL</span>
              <ChevronRight className="w-5 h-5" />
            </button>
          </div>
        </motion.div>

        {/* Feature Grid */}
        <div className="grid grid-cols-3 gap-8 mt-48 w-full">
          {[
            { title: "TRI-FOLD CORE", icon: Shield, desc: "Constitution, Store, and Jarvis Engine in mathematical alignment." },
            { title: "PERMANENT SWARM", icon: Cpu, desc: "24/7 background daemons for continuous operations." },
            { title: "OMEGA VAULT", icon: Lock, desc: "5-point MFA security for absolute Pilot verification." }
          ].map((feature, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.2 + i * 0.1 }}
              className="glass p-8 rounded-[2rem] text-left group hover:bg-white/[0.05] transition-colors"
            >
              <div className="w-12 h-12 rounded-2xl bg-omega-500/10 flex items-center justify-center mb-6 group-hover:bg-omega-500/20 transition-colors">
                <feature.icon className="w-6 h-6 text-omega-400" />
              </div>
              <h3 className="text-lg font-bold mb-2 tracking-tight">{feature.title}</h3>
              <p className="text-sm text-white/40 leading-relaxed font-medium">{feature.desc}</p>
            </motion.div>
          ))}
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-white/5 p-8 max-w-7xl mx-auto flex justify-between items-center text-[10px] font-bold tracking-widest text-white/20">
        <span>© 2026 OMEGA SYSTEM PROTOCOL</span>
        <div className="flex space-x-8">
          <a href="#" className="hover:text-white transition-colors">GITHUB</a>
          <a href="#" className="hover:text-white transition-colors">DOCUMENTATION</a>
          <a href="#" className="hover:text-white transition-colors">SECURITY</a>
        </div>
      </footer>
    </div>
  );

  const AuthVault = () => (
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

  const Dashboard = () => (
    <div className="min-h-screen bg-black flex text-white/90">
      {/* Sidebar */}
      <div className="w-72 glass border-r border-white/5 p-6 flex flex-col space-y-8">
        <div className="flex items-center justify-between px-2">
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 rounded-lg omega-gradient flex items-center justify-center">
              <Shield className="w-5 h-5 text-white" />
            </div>
            <span className="font-bold text-xl tracking-tighter">JARVIS v2.1</span>
          </div>
          <button onClick={() => setView("landing")} className="text-white/20 hover:text-white transition-colors">
            <X className="w-4 h-4" />
          </button>
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
              className={`w-full flex items-center space-x-3 px-4 py-3 rounded-xl transition-all ${activeTab === item.id ? "bg-white/10 text-omega-400 font-bold shadow-[inset_0_0_10px_rgba(14,165,233,0.1)]" : "hover:bg-white/5 text-white/50"
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
        <AnimatePresence mode="wait">
          <motion.div
            key={activeTab}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
          >
            {activeTab === "mission" && (
              <div className="grid grid-cols-4 gap-6">
                {["PENDING", "BUILDING", "BLOCKED", "STABLE"].map((status) => (
                  <div key={status} className="space-y-4">
                    <div className="flex items-center justify-between px-1">
                      <span className="text-[10px] font-bold tracking-widest text-white/30">{status}</span>
                      <span className="text-[10px] font-mono text-omega-500">2</span>
                    </div>
                    <div className="min-h-[200px] glass rounded-2xl p-2 space-y-2">
                      <div className="p-4 bg-white/5 rounded-xl border border-white/5 hover:border-omega-500/30 transition-colors cursor-pointer group">
                        <h4 className="text-sm font-bold group-hover:text-omega-400 uppercase tracking-tight">Initialize Master UI</h4>
                        <p className="text-[10px] text-white/40 mt-2 font-mono">ID: OM-964</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}

            {activeTab === "memory" && (
              <div className="glass rounded-3xl p-8 min-h-[400px] flex items-center justify-center">
                <div className="text-center space-y-4">
                  <Database className="w-12 h-12 text-white/10 mx-auto" />
                  <p className="text-white/20 italic font-light">Accessing Hippocampus... Memory retrieval in progress.</p>
                </div>
              </div>
            )}
          </motion.div>
        </AnimatePresence>
      </main>
    </div>
  );

  return (
    <AnimatePresence mode="wait">
      {view === "landing" && LandingPage()}
      {view === "auth" && AuthVault()}
      {view === "dashboard" && Dashboard()}
    </AnimatePresence>
  );
}
