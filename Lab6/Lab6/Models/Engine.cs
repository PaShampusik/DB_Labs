using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Engine
    {
        public Engine()
        {
            Products = new HashSet<Product>();
        }

        public int Id { get; set; }
        public string Name { get; set; } = null!;
        public string Volume { get; set; } = null!;

        public virtual ICollection<Product> Products { get; set; }
    }
}
