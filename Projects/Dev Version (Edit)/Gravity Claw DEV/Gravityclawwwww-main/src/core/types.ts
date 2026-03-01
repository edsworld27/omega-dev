export interface Message {
  id: string;
  channelId: string;
  userId: string;
  text: string;
  media?: string[];
  replyToId?: string;
  isVoice?: boolean;
}

export interface Provider {
  name: string;
  generateResponse(context: Message[], systemPrompt: string): Promise<string>;
  generateToolCalls?(context: Message[], tools: Tool[]): Promise<any>;
}

export interface Channel {
  name: string;
  initialize(router: MessageRouter): Promise<void>;
  sendMessage(toUserId: string, text: string, media?: string[]): Promise<void>;
  sendVoiceMessage?(toUserId: string, audioBuffer: Buffer): Promise<void>;
  sendTypingStatus?(toUserId: string): Promise<void>;
}

export interface Tool {
  name: string;
  description: string;
  parameters: any; // JSON Schema string or object for tool parameters
  execute(params: any): Promise<any>;
}

export interface MemoryPlugin {
  name: string;
  initialize(): Promise<void>;
  storeMessage(msg: Message): Promise<void>;
  retrieveContext(userId: string, limit?: number): Promise<Message[]>;
}

export interface MessageRouter {
  handleIncomingMessage(msg: Message, channel: Channel): Promise<void>;
  registerChannel(channel: Channel): void;
}
