using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Review
    {
        public int Id { get; set; }
        public int? UserId { get; set; }
        public string? Text { get; set; }
        public int Rating { get; set; }

        public virtual User? User { get; set; }
    }
}
