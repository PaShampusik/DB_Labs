using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Order
    {
        public int Id { get; set; }
        public int Sum { get; set; }
        public int UserId { get; set; }
        public int ProductId { get; set; }
        public DateTime Time { get; set; }
        public int StatusId { get; set; }

        public virtual Product Product { get; set; } = null!;
        public virtual OrderStatus Status { get; set; } = null!;
        public virtual User User { get; set; } = null!;
    }
}
