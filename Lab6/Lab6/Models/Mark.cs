using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Mark
    {
        public Mark()
        {
            Models = new HashSet<Model>();
        }

        public int Id { get; set; }
        public string Name { get; set; } = null!;
        public string PlaceOfProduction { get; set; } = null!;

        public virtual ICollection<Model> Models { get; set; }
    }
}
