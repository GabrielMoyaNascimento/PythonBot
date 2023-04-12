<?php
namespace App\Http\Controllers;
   
use BotMan\BotMan\BotMan;
use Illuminate\Http\Request;
use BotMan\BotMan\Messages\Incoming\Answer;
   
class BotManController extends Controller
{
    /**
     * Place your BotMan logic here.
     */
    public function handle()
    {
        $botman = app('botman');
        
        $botman->hears('{message}', function($botman, $message) {
   
            if ($message == 'Olá') {
                $this->askName($botman);
            }
            if ($message == 'Turing') {
                $botman->reply('O teste de Turing é baseado em uma conversa entre uma máquina e um ser humano, que deve determinar se as respostas da máquina são ou não indistinguíveis das respostas de um ser humano.');
            }
            if ($message == 'IFPR') {
                $botman->reply('O IFPR campus Paranavaí foi criado em 2008, a partir da expansão da rede federal de educação profissional e tecnológica. Desde então, tem oferecido ensino de qualidade e formado profissionais capacitados para o mercado de trabalho.');
            }

            else{
                $botman->reply("
                    Olá, digite uma das opções abaixo para que eu possa te auxiliar melhor,
                    Você deseja:
                    1 - 'Turing' - Conhecer mais sobre Alan Turing e o teste de turing
                    2 - 'IFPR' - Saber uma curiosidade sobre o campus   Paranavaí
                    3 - ' Olá' - Perguntarei o seu nome para te cumprimentar
                ");
            }
   
        });
   
        $botman->listen();
    }
   
    /**
     * Place your BotMan logic here.
     */
    public function askName($botman)
    {
        $botman->ask('Olá, qual o seu nome?', function(Answer $answer) {
   
            $name = $answer->getText();
   
            $this->say('Prazer em te conhecer '.$name);
        });  
    }
}