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
            
            else{
                $botman->reply("Diga 'Olá' para iniciar...");
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