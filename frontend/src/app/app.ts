import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

interface Book {
  title: string;
  author: string;
  category: string;
  price: string;
  description: string;
}

interface ChatResponse {
  message: string;
  books: Book[];
}

interface ChatMessage {
  type: 'user' | 'bot';
  text: string;
  books?: Book[];
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {

  message = '';

  messages: ChatMessage[] = [
    {
      type: 'bot',
      text: 'Olá! Sou o assistente virtual da livraria. Como posso ajudar?'
    }
  ];

  loading = false;

  constructor(private http: HttpClient) {}

  sendMessage(): void {

    const text = this.message.trim();

    if (!text || this.loading) {
      return;
    }

    // Adiciona a mensagem do usuário
    this.messages.push({
      type: 'user',
      text: text
    });

    this.message = '';
    this.loading = true;

    this.http.post<ChatResponse>(
      'http://127.0.0.1:8000/api/chat/',
      {
        message: text
      }
    ).subscribe({

      next: (response) => {

        this.messages.push({
          type: 'bot',
          text: response.message,
          books: response.books
        });

        this.loading = false;
      },

      error: (error) => {

        console.error(error);

        this.messages.push({
          type: 'bot',
          text: 'Desculpe, ocorreu um erro ao consultar a livraria.'
        });

        this.loading = false;
      }

    });
  }
}