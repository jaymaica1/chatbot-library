import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ChatService } from './services/chat.service';

interface Message {
  text: string;
  sender: 'user' | 'assistant';
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {

  message = '';

  messages: Message[] = [
    {
      text: 'Olá! 👋 Posso ajudar você a encontrar livros na nossa livraria.',
      sender: 'assistant'
    }
  ];

  loading = false;

  constructor(private chatService: ChatService) {}

  sendMessage(): void {

    if (!this.message.trim() || this.loading) {
      return;
    }

    const userMessage = this.message.trim();

    this.messages.push({
      text: userMessage,
      sender: 'user'
    });

    this.message = '';
    this.loading = true;

    this.chatService.sendMessage(userMessage).subscribe({

      next: (response) => {

        this.messages.push({
          text: response.message,
          sender: 'assistant'
        });

        this.loading = false;
      },

      error: (error) => {

        console.error(error);

        this.messages.push({
          text: 'Desculpe, ocorreu um erro ao tentar responder.',
          sender: 'assistant'
        });

        this.loading = false;
      }

    });
  }
}
