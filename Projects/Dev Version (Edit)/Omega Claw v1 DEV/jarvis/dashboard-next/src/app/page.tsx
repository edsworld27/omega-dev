"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Shield, Mail, Phone, Lock, Cpu, LayoutDashboard,
  Database, Activity, Settings, ChevronRight,
  Download, Github, Terminal, Activity as ActivityIcon,
  X, Copy, CheckCircle2, Server, Globe, Fingerprint
} from "lucide-react";

export default function Home() {
  const [view, setView] = useState("landing"); // landing, auth, dashboard
  const [authStep, setAuthStep] = useState(1);
  const [activeTab, setActiveTab] = useState("mission");
  const [isAutoPilot, setIsAutoPilot] = useState(false);
  const [showDownloads, setShowDownloads] = useState(false);
  const [copied, setCopied] = useState(false);

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
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  // --- COMPONENTS ---

  const LandingPage = () => (
    <div className="min-h-screen bg-[#050505] text-white selection:bg-omega-500/30 overflow-hidden relative">
      {/* Background Ambience */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
        <div className="absolute top-[-20%] right-[-10%] w-[60%] h-[60%] bg-omega-500/5 blur-[150px] rounded-full animate-pulse" />
        <div className="absolute bottom-[-20%] left-[-10%] w-[40%] h-[40%] bg-omega-900/10 blur-[120px] rounded-full" />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1px] h-full bg-gradient-to-b from-transparent via-white/5 to-transparent" />
      </div>

      {/* Navigation */}
      <nav className="flex items-center justify-between p-10 max-w-7xl mx-auto relative z-20 stagger-item" style={{ animationDelay: "0.1s" }}>
        <div className="flex items-center space-x-4">
          <div className="w-12 h-12 rounded-2xl omega-gradient flex items-center justify-center shadow-[0_0_30px_rgba(14,165,233,0.3)]">
            <Shield className="w-7 h-7 text-white" />
          </div>
          <div className="flex flex-col">
            <span className="font-black text-2xl tracking-tighter leading-none">OMEGA</span>
            <span className="text-[10px] font-bold tracking-[0.3em] text-omega-400 mt-1">SYSTEMS</span>
          </div>
        </div>

        <div className="flex items-center space-x-10">
          <div className="relative">
            <button
              onClick={() => setShowDownloads(!showDownloads)}
              className="text-[11px] font-black tracking-widest text-white/40 hover:text-white transition-colors flex items-center space-x-2"
            >
              <span>ACCESS REPOSITORIES</span>
              <ChevronRight className={`w-3 h-3 transition-transform ${showDownloads ? "rotate-90" : ""}`} />
            </button>
            <AnimatePresence>
              {showDownloads && (
                <motion.div
                  initial={{ opacity: 0, scale: 0.95, y: 10 }}
                  animate={{ opacity: 1, scale: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.95, y: 10 }}
                  transition={{ type: "spring", stiffness: 300, damping: 30 }}
                  className="absolute top-full right-0 mt-6 w-72 glass rounded-[2rem] p-3 shadow-2xl z-30"
                >
                  <a href="https://github.com/edsworld27/Omega-System" target="_blank" className="flex items-center justify-between p-4 hover:bg-white/5 rounded-2xl transition-all group">
                    <div className="flex items-center space-x-3">
                      <Globe className="w-4 h-4 text-omega-400" />
                      <span className="text-xs font-bold">System Core</span>
                    </div>
                    <ExternalLink className="w-3 h-3 text-white/20 group-hover:text-white/40" />
                  </a>
                  <a href="https://github.com/edsworld27/omega-claw" target="_blank" className="flex items-center justify-between p-4 hover:bg-white/5 rounded-2xl transition-all group">
                    <div className="flex items-center space-x-3">
                      <Cpu className="w-4 h-4 text-omega-400" />
                      <span className="text-xs font-bold">AGI Engine</span>
                    </div>
                    <ExternalLink className="w-3 h-3 text-white/20 group-hover:text-white/40" />
                  </a>
                  <div className="h-[1px] bg-white/5 my-2 mx-2" />
                  <button onClick={copyInstallCmd} className="w-full flex items-center justify-between p-4 hover:bg-white/5 rounded-2xl transition-all">
                    <div className="flex items-center space-x-3">
                      <Terminal className="w-4 h-4 text-omega-400" />
                      <span className="text-xs font-bold">Quick Install</span>
                    </div>
                    {copied ? <CheckCircle2 className="w-4 h-4 text-green-500" /> : <Copy className="w-3 h-3 text-white/20" />}
                  </button>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
          <button
            onClick={handleLoginStart}
            className="px-8 py-3 glass rounded-2xl text-[11px] font-black tracking-widest hover:bg-white/10 transition-all border border-white/10"
          >
            ENTER VAULT
          </button>
        </div>
      </nav>

      {/* Hero */}
      <main className="max-w-7xl mx-auto px-10 pt-32 pb-40 relative z-10 flex flex-col items-center text-center">
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
          className="space-y-10"
        >
          <div className="inline-flex items-center space-x-3 px-4 py-2 bg-white/5 border border-white/10 rounded-full">
            <div className="w-2 h-2 rounded-full bg-omega-500 animate-ping" />
            <span className="text-[10px] font-black tracking-[0.25em] text-white/60">PROTOCOLS ALIGNED</span>
          </div>

          <h1 className="text-[120px] font-black tracking-[-0.05em] leading-[0.85] text-gradient">
            THE OMEGA <br /> <span className="text-omega-500">NEXUS</span>
          </h1>

          <p className="max-w-3xl mx-auto text-2xl text-white/40 font-medium leading-tight">
            Deploying the first resilient Tri-Fold AGI architecture. <br />
            Hardened locally. Scaled globally.
          </p>

          <div className="flex items-center justify-center pt-10">
            <button
              onClick={handleLoginStart}
              className="px-12 py-6 omega-gradient rounded-3xl font-black text-xl shadow-[0_30px_60px_-15px_rgba(14,165,233,0.5)] hover:scale-105 transition-all active:scale-95 flex items-center space-x-4 group"
            >
              <span>IGNITE MISSION CONTROL</span>
              <ChevronRight className="w-6 h-6 group-hover:translate-x-1 transition-transform" />
            </button>
          </div>
        </motion.div>

        {/* Feature Triggers */}
        <div className="grid grid-cols-3 gap-10 mt-52 w-full">
          {[
            { title: "TRI-FOLD ARCHITECTURE", icon: Shield, desc: "A immutable Constitution governing a modular Store and an autonomous Jarvis engine." },
            { title: "PERMANENT SWARM", icon: Cpu, desc: "Deploy background daemons that never sleep, handling outreach and surveillance 24/7." },
            { title: "SECURE LOCALITY", icon: Server, desc: "Zero external dependencies. Your data and intelligence live exclusively on your hardware." }
          ].map((feature, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4 + i * 0.1, type: "spring", stiffness: 100 }}
              className="glass p-12 rounded-[3.5rem] text-left hover-lift group border border-white/5"
            >
              <div className="w-14 h-14 rounded-2xl bg-omega-500/10 flex items-center justify-center mb-10 group-hover:bg-omega-500/20 transition-all shadow-inner">
                <feature.icon className="w-7 h-7 text-omega-400" />
              </div>
              <h3 className="text-xl font-black mb-4 tracking-tighter">{feature.title}</h3>
              <p className="text-base text-white/30 leading-snug font-medium">{feature.desc}</p>
            </motion.div>
          ))}
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-white/5 p-12 max-w-7xl mx-auto flex justify-between items-center relative z-10">
        <div className="flex items-center space-x-3 text-[10px] font-black tracking-widest text-white/10 uppercase">
          <span>STABLE RELEASE</span>
          <div className="w-1 h-1 rounded-full bg-white/10" />
          <span>AGI-001</span>
        </div>
        <div className="flex space-x-12">
          {["SYNOPSIS", "CONSTITUTION", "SECURITY", "LEGAL"].map((link) => (
            <a key={link} href="#" className="text-[10px] font-black tracking-widest text-white/20 hover:text-omega-400 transition-colors">{link}</a>
          ))}
        </div>
      </footer>
    </div>
  );

  const AuthVault = () => (
    <div className="min-h-screen flex items-center justify-center p-4 bg-[#050505] relative overflow-hidden">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-omega-500/5 blur-[120px] rounded-full" />

      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="w-full max-w-lg p-12 glass rounded-[3rem] space-y-10 relative z-10 shadow-2xl"
      >
        <div className="flex flex-col items-center space-y-6">
          <div className="relative">
            <div className="absolute inset-0 bg-omega-400/20 blur-2xl rounded-full animate-pulse" />
            <div className="relative p-6 bg-omega-500/10 rounded-3xl border border-omega-500/20">
              <Fingerprint className="w-14 h-14 text-omega-400" />
            </div>
          </div>
          <div className="text-center space-y-2">
            <h1 className="text-3xl font-black tracking-tighter">SECURITY CHAMBER</h1>
            <p className="text-omega-400/60 text-xs font-black tracking-widest uppercase">Layer {authStep} of 5 Persistence Check</p>
          </div>
        </div>

        <AnimatePresence mode="wait">
          <motion.div
            key={authStep}
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            transition={{ type: "spring", stiffness: 300, damping: 30 }}
            className="space-y-8"
          >
            <div className="space-y-6">
              <div className="flex items-center space-x-3 text-omega-300">
                {authStep <= 3 && <Mail className="w-5 h-5" />}
                {authStep === 4 && <Phone className="w-5 h-5" />}
                {authStep === 5 && <Cpu className="w-5 h-5" />}
                <span className="text-sm font-bold tracking-tight">
                  {authStep <= 3 && `Sequence Token ID: 00${authStep}`}
                  {authStep === 4 && "Hardware Authentication"}
                  {authStep === 5 && "Neural Handshake"}
                </span>
              </div>

              <div className="space-y-4">
                {authStep === 5 && <p className="text-xs text-white/30 font-medium">Identify the primary protocol of the Omega Seed.</p>}
                <input
                  type={authStep === 5 ? "text" : "password"}
                  placeholder={authStep === 5 ? "Protocol ID..." : "••••••••"}
                  className="w-full bg-white/5 border border-white/10 rounded-2xl p-6 text-xl font-mono text-center outline-none focus:border-omega-500 focus:bg-omega-500/5 transition-all"
                  autoFocus
                />
              </div>
            </div>

            <button
              onClick={handleAuth}
              className="w-full py-6 rounded-2xl omega-gradient font-black text-lg shadow-[0_20px_40px_-10px_rgba(14,165,233,0.3)] hover:opacity-90 transition-all active:scale-95"
            >
              VALIDATE PILOT
            </button>
          </motion.div>
        </AnimatePresence>

        <button
          onClick={() => setView("landing")}
          className="w-full text-center text-white/20 text-[10px] font-black tracking-[0.3em] uppercase hover:text-white/40 transition-colors"
        >
          Cancel Operation
        </button>
      </motion.div>
    </div>
  );

  const Dashboard = () => (
    <div className="min-h-screen bg-[#050505] flex text-white overflow-hidden">
      {/* Sidebar */}
      <div className="w-80 glass border-r border-white/5 p-8 flex flex-col space-y-12">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="w-10 h-10 rounded-xl omega-gradient flex items-center justify-center shadow-lg">
              <Shield className="w-6 h-6 text-white" />
            </div>
            <div className="flex flex-col">
              <span className="font-black text-xl tracking-tighter leading-none">JARVIS</span>
              <span className="text-[10px] font-bold tracking-widest text-omega-400 opacity-60">MISSION CONTROL</span>
            </div>
          </div>
        </div>

        <nav className="flex-1 space-y-3">
          {[
            { id: "mission", name: "Operations Board", icon: LayoutDashboard },
            { id: "memory", name: "Pattern Memory", icon: Database },
            { id: "hive", name: "Hive Monitoring", icon: ActivityIcon },
            { id: "settings", name: "System Setup", icon: Settings },
          ].map((item) => (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center space-x-4 px-6 py-4 rounded-2xl transition-all group ${activeTab === item.id
                  ? "bg-white/5 text-omega-400 font-black shadow-[inset_0_0_20px_rgba(14,165,233,0.05)] border border-omega-500/20"
                  : "text-white/30 hover:bg-white/[0.02] hover:text-white/60"
                }`}
            >
              <item.icon className={`w-5 h-5 transition-transform ${activeTab === item.id ? "scale-110" : "group-hover:scale-110"}`} />
              <span className="text-sm tracking-tight">{item.name}</span>
            </button>
          ))}
        </nav>

        <div className="space-y-6">
          <div className="p-6 glass rounded-3xl space-y-5 border border-white/5">
            <div className="flex items-center justify-between">
              <span className="text-[10px] font-black tracking-widest text-white/30 uppercase">Auto-Pilot</span>
              <button
                onClick={() => setIsAutoPilot(!isAutoPilot)}
                className={`w-12 h-6 rounded-full transition-all p-1 ${isAutoPilot ? "bg-omega-500 shadow-[0_0_15px_rgba(14,165,233,0.4)]" : "bg-white/10"}`}
              >
                <div className={`w-4 h-4 rounded-full bg-white transition-all shadow-md ${isAutoPilot ? "translate-x-6" : "translate-x-0"}`} />
              </button>
            </div>
            <div className="flex items-center space-x-3 text-[10px] font-black tracking-widest text-omega-400">
              <div className="w-2 h-2 rounded-full bg-omega-500 animate-pulse shadow-[0_0_8px_#0ea5e9]" />
              <span>NEXUS CONNECTED</span>
            </div>
          </div>

          <button
            onClick={() => setView("landing")}
            className="w-full py-4 text-xs font-black tracking-[0.2em] text-white/10 hover:text-red-500/40 transition-colors uppercase flex items-center justify-center space-x-2"
          >
            <Power className="w-4 h-4" />
            <span>Hibernate</span>
          </button>
        </div>
      </div>

      {/* Main */}
      <main className="flex-1 p-12 space-y-12 overflow-y-auto">
        <header className="flex justify-between items-end">
          <div className="space-y-2">
            <h2 className="text-4xl font-black tracking-tight text-white">
              {activeTab === "mission" && "Active Operations"}
              {activeTab === "memory" && "Pattern Lab"}
              {activeTab === "hive" && "Swarm Surveillance"}
              {activeTab === "settings" && "Security Vault"}
            </h2>
            <div className="flex items-center space-x-2 text-white/20 text-[10px] font-black tracking-[0.2em] uppercase">
              <span>Ground Truth</span>
              <div className="w-1 h-1 rounded-full bg-white/10" />
              <span>v2.11 Release</span>
            </div>
          </div>
          <div className="flex space-x-6">
            <button className="px-8 py-3.5 glass rounded-2xl text-[11px] font-black tracking-widest hover:bg-white/10 transition-all">
              SNAPSHOT SYSTEM
            </button>
            <button className="px-8 py-3.5 omega-gradient rounded-2xl text-[11px] font-black tracking-widest shadow-xl hover:scale-105 transition-all">
              GLOBAL SYNC
            </button>
          </div>
        </header>

        <AnimatePresence mode="wait">
          <motion.div
            key={activeTab}
            initial={{ opacity: 0, scale: 0.98, y: 10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.98, y: -10 }}
            transition={{ type: "spring", stiffness: 200, damping: 25 }}
            className="w-full"
          >
            {activeTab === "mission" && (
              <div className="grid grid-cols-4 gap-8">
                {["STAGING", "ACTIVE", "BLOCKED", "RESOLVED"].map((status) => (
                  <div key={status} className="space-y-6">
                    <div className="flex items-center justify-between px-2">
                      <span className="text-[11px] font-black tracking-[0.3em] text-white/20 uppercase">{status}</span>
                      <div className="px-2 py-1 glass rounded-md text-[9px] font-mono text-omega-500">02</div>
                    </div>
                    <div className="min-h-[500px] glass rounded-[2.5rem] p-4 space-y-4 border border-white/5">
                      {[1, 2].map((i) => (
                        <motion.div
                          key={i}
                          whileHover={{ scale: 1.02 }}
                          className="p-6 bg-white/[0.03] rounded-3xl border border-white/5 hover:border-omega-500/30 transition-all cursor-pointer group hover:bg-white/[0.05]"
                        >
                          <h4 className="text-xs font-black group-hover:text-omega-400 transition-colors tracking-tight uppercase">Master UI Redesign</h4>
                          <p className="text-[10px] text-white/20 mt-3 font-mono leading-relaxed">Task: Integrate Website Kit tokens and springs.</p>
                          <div className="mt-4 pt-4 border-t border-white/5 flex justify-between items-center text-[9px] font-bold text-white/10">
                            <span>PRIORITY: HIGH</span>
                            <span>#OM-kit</span>
                          </div>
                        </motion.div>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            )}

            {activeTab === "memory" && (
              <div className="glass rounded-[3.5rem] p-16 min-h-[500px] flex items-center justify-center border border-white/5">
                <div className="text-center space-y-8">
                  <div className="w-20 h-20 rounded-[2rem] bg-omega-500/5 flex items-center justify-center mx-auto border border-omega-500/20">
                    <Database className="w-10 h-10 text-omega-400/40" />
                  </div>
                  <div className="space-y-2">
                    <p className="text-2xl font-black tracking-tight text-white/40">MEMORY SYNC IN PROGRESS</p>
                    <p className="text-white/10 text-[10px] font-black tracking-[0.4em] uppercase">Accessing Hippocampus Patterns</p>
                  </div>
                </div>
              </div>
            )}
          </motion.div>
        </AnimatePresence>
      </main>
    </div>
  );

  return (
    <div className="font-sans">
      <AnimatePresence mode="wait">
        {view === "landing" && LandingPage()}
        {view === "auth" && AuthVault()}
        {view === "dashboard" && Dashboard()}
      </AnimatePresence>
    </div>
  );
}

const Power = ({ className }) => <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><path d="M12 2v10" /><path d="M18.4 6.6a9 9 0 1 1-12.77.04" /></svg>;
