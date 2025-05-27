public class Cachorro
{
      public Cachorro(string nome, int idade)
      {
          Nome = nome;
          Idade = idade;
      }
      public string Nome { get; protected set; } =
“Canelinha”;
      public int Idade { get; set; } = 1;
      public void IncrementaIdade() => Idade++;

      public int IdadeDoCachorroEmAnos() => Idade * 7;
}